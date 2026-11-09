/* Golden Life — host-bg-1. Local surface detection; no preference-based decision.
 * Dark CSS MUST be gated on [data-gl-site-scheme="dark"] on the supported root.
 * Without this script the stylesheet must remain light. No photographs are changed.
 * See analysis/README.cs.md for paint-model limits and offline verification.
 */
(function (window, document) {
  'use strict';
  var VERSION = 'host-bg-1';
  var previous = window.GoldenLifeProductScheme;
  if (previous && previous.version === VERSION && typeof previous.refresh === 'function') {
    previous.refresh();
    return;
  }
  // Do not silently replace another initializer with an incompatible contract.
  if (previous) return;

  var THEMES = Object.freeze([
    'beauty-star', 'slim-extreme-collagen-box-ananas', 'beauty-longevity',
    'woman-hormonal-balance', 'glp1-woman-balance', 'glp1-woman-balance-sacek',
    'anti-age-longevity', 'beauty-longevity-sacek', 'slim-extreme-collagen',
    'slim-sos-fat-burner', 'slim-glp-1-activator',
    'slim-extreme-collagen-sacek-ananas', 'slim-extreme-collagen-box-ananas-mango',
    'slim-extreme-collagen-sacek-ananas-mango'
  ]);
  var supported = new Set(THEMES);
  var ATTRIBUTE = 'data-gl-site-scheme';
  var THRESHOLD = 0.179;
  var POLL_MS = 1500;
  var UPDATE_MS = 80; // Fixed, not sliding: mutation bursts cannot postpone forever.
  var pending = null;
  var poll = null;
  var shadowTrees = new Set();
  var ownedRoots = new Set();
  var probeHost = null;
  var probe = null;
  var canvasContext = null;
  var refreshing = false;

  function isSupported(root) {
    return !!root && root.nodeType === 1 && root.ownerDocument === document &&
      supported.has(root.getAttribute('data-gl-theme'));
  }
  function parentOf(element) {
    if (element.assignedSlot) return element.assignedSlot;
    if (element.parentElement) return element.parentElement;
    var tree = element.getRootNode();
    return tree && tree.host ? tree.host : null;
  }
  function color(raw) {
    if (!raw) return null;
    if (raw === 'transparent') return [0, 0, 0, 0];
    var match = /^rgba?\(([^)]+)\)$/i.exec(raw.trim());
    if (match) {
      var parts = match[1].replace(/,/g, ' ').replace(/\//g, ' ').trim().split(/\s+/);
      if (parts.length === 3 || parts.length === 4) {
        var rgb = parts.slice(0, 3).map(function (v) {
          return Math.max(0, Math.min(255, parseFloat(v) * (/%$/.test(v) ? 2.55 : 1)));
        });
        var a = parts.length === 4 ? parseFloat(parts[3]) * (/%$/.test(parts[3]) ? 0.01 : 1) : 1;
        if (rgb.every(Number.isFinite) && Number.isFinite(a)) return rgb.concat(Math.max(0, Math.min(1, a)));
      }
    }
    // CSS Color 4 computed values need not serialize as rgb(). Convert a solid
    // colour only, locally, to the sRGB space used by the luminance threshold.
    try {
      if (!window.CSS || !window.CSS.supports('color', raw)) return null;
      if (!canvasContext) canvasContext = document.createElement('canvas').getContext('2d', {willReadFrequently: true});
      if (!canvasContext) return null;
      canvasContext.clearRect(0, 0, 1, 1);
      canvasContext.fillStyle = raw;
      canvasContext.fillRect(0, 0, 1, 1);
      var pixel = canvasContext.getImageData(0, 0, 1, 1).data;
      return [pixel[0], pixel[1], pixel[2], pixel[3] / 255];
    } catch (_) { return null; }
  }
  function over(front, back) {
    var a = front[3] + back[3] * (1 - front[3]);
    if (!a) return [0, 0, 0, 0];
    return [0, 1, 2].map(function (i) {
      return (front[i] * front[3] + back[i] * back[3] * (1 - front[3])) / a;
    }).concat(a);
  }
  function luminance(rgba) {
    var linear = rgba.slice(0, 3).map(function (v) {
      v /= 255;
      return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2];
  }
  function canvasColor() {
    if (!document.documentElement) return null;
    if (!probeHost || !probeHost.isConnected) {
      probeHost = document.createElement('span');
      probeHost.setAttribute('aria-hidden', 'true');
      probeHost.style.cssText = 'all:initial!important;display:block!important;position:fixed!important;left:0!important;top:0!important;width:0!important;height:0!important;overflow:hidden!important;visibility:hidden!important;pointer-events:none!important;contain:strict!important;';
      var isolated = probeHost.attachShadow({mode: 'closed'});
      probe = document.createElement('span');
      probe.style.cssText = 'all:initial!important;background-color:Canvas!important;display:block!important;';
      isolated.appendChild(probe);
      // Prefer HEAD so BODY retains its sibling/last-child relationships.
      (document.head || document.documentElement).appendChild(probeHost);
    }
    // The underlying document canvas uses HTML's scheme, NOT the product's or
    // a transparent wrapper's local colour-scheme. Canvas resolves UA paint.
    var scheme = window.getComputedStyle(document.documentElement).colorScheme || 'normal';
    probe.style.setProperty('color-scheme', scheme, 'important');
    return color(window.getComputedStyle(probe).backgroundColor);
  }
  function result(scheme, rgba, reason, count, usedCanvas) {
    return {
      scheme: scheme,
      rgba: rgba,
      luminance: rgba ? luminance(rgba) : null,
      reason: reason,
      sampledAncestors: count,
      usedCanvas: !!usedCanvas,
      threshold: THRESHOLD
    };
  }
  function unknown(reason, count) { return result('light', null, reason, count, false); }
  function inspect(root) {
    if (!isSupported(root)) return unknown('unsupported-root', 0);
    if (!root.isConnected) return unknown('disconnected-root', 0);
    try {
      var chain = [];
      var visited = new Set();
      // Never inspect the product's OWN background: dark product CSS may paint
      // it black. Sampling it would latch dark forever after a host change.
      for (var node = parentOf(root); node && !visited.has(node); node = parentOf(node)) {
        visited.add(node);
        var style = window.getComputedStyle(node);
        chain.push(style);
        // Group compositing can alter even an opaque nearer panel. Do not claim
        // a resolved colour for a paint operation this model cannot calculate.
        if (Number(style.opacity) !== 1 || style.filter !== 'none' ||
            (style.backdropFilter && style.backdropFilter !== 'none') ||
            (style.mixBlendMode && style.mixBlendMode !== 'normal') ||
            (style.maskImage && style.maskImage !== 'none')) {
          return unknown('unknown-compositing-effect', chain.length);
        }
      }
      var resolved = [0, 0, 0, 0];
      var sampled = 0;
      for (var i = 0; i < chain.length; i++) {
        var current = chain[i];
        sampled++;
        if (current.backgroundImage !== 'none') return unknown('unknown-background-image', sampled);
        if (current.backgroundClip && /\btext\b/.test(current.backgroundClip)) return unknown('unknown-background-clip', sampled);
        var layer = color(current.backgroundColor);
        if (!layer) return unknown('unknown-background-color', sampled);
        resolved = over(resolved, layer);
        if (resolved[3] >= 1) break;
      }
      var usedCanvas = resolved[3] < 1;
      if (usedCanvas) {
        var canvas = canvasColor();
        if (!canvas || canvas[3] < 1) return unknown('unknown-ua-canvas', sampled);
        resolved = over(resolved, canvas);
      }
      return result(luminance(resolved) < THRESHOLD ? 'dark' : 'light', resolved,
        usedCanvas ? 'ua-canvas' : 'ancestor-background', sampled, usedCanvas);
    } catch (_) { return unknown('unresolved-style', 0); }
  }

  function visible() { return document.visibilityState !== 'hidden'; }
  function schedule() {
    if (!visible() || pending !== null) return;
    pending = window.setTimeout(function () { pending = null; refresh(); }, UPDATE_MS);
  }
  var observer = new MutationObserver(function (records) {
    for (var i = 0; i < records.length; i++) {
      var record = records[i];
      if (record.target === probeHost) continue;
      // Our one output attribute is deliberately not a trigger. All other
      // attributes are observed because arbitrary site CSS may depend on them.
      if (record.type === 'attributes' && record.attributeName === ATTRIBUTE) continue;
      schedule();
      break;
    }
  });
  var observedEvents = ['load', 'error', 'transitionrun', 'transitionend', 'transitioncancel',
    'animationstart', 'animationiteration', 'animationend', 'slotchange'];
  function listen(tree, add) {
    observedEvents.forEach(function (event) {
      tree[add ? 'addEventListener' : 'removeEventListener'](event, schedule, true);
    });
  }
  function armPoll() {
    if (poll !== null || !visible()) return;
    poll = window.setTimeout(function () {
      poll = null;
      if (visible()) refresh();
    }, POLL_MS);
  }
  function refresh() {
    if (refreshing) return {roots: ownedRoots.size, updated: 0};
    refreshing = true;
    if (pending !== null) { window.clearTimeout(pending); pending = null; }
    var foundRoots = new Set();
    var foundShadows = new Set();
    var updated = 0;
    try {
      function discover(tree) {
        tree.querySelectorAll('*').forEach(function (element) {
          if (isSupported(element)) foundRoots.add(element);
          if (element.shadowRoot) {
            foundShadows.add(element.shadowRoot);
            discover(element.shadowRoot);
          }
        });
      }
      discover(document);
      var changed = foundShadows.size !== shadowTrees.size;
      foundShadows.forEach(function (tree) { if (!shadowTrees.has(tree)) changed = true; });
      if (changed) {
        observer.disconnect();
        shadowTrees.forEach(function (tree) { if (!foundShadows.has(tree)) listen(tree, false); });
        foundShadows.forEach(function (tree) { if (!shadowTrees.has(tree)) listen(tree, true); });
        shadowTrees = foundShadows;
        observe(document);
        shadowTrees.forEach(observe);
      }
      // Only currently supported roots are ever written. Attributes on an
      // unsupported (including subsequently re-labelled) root belong to its
      // owner; dark CSS must independently include the supported theme gate.
      foundRoots.forEach(function (root) {
        var resolved = inspect(root);
        if (root.getAttribute(ATTRIBUTE) !== resolved.scheme) {
          root.setAttribute(ATTRIBUTE, resolved.scheme);
          updated++;
        }
      });
      ownedRoots = foundRoots;
      return {roots: foundRoots.size, updated: updated};
    } finally {
      refreshing = false;
      armPoll();
    }
  }
  function observe(tree) {
    observer.observe(tree, {subtree: true, childList: true, attributes: true, characterData: true});
  }
  window.GoldenLifeProductScheme = Object.freeze({
    version: VERSION,
    supportedThemes: THEMES,
    refresh: refresh,
    inspect: inspect
  });
  observe(document);
  listen(document, true);
  window.addEventListener('resize', schedule, {passive: true});
  window.addEventListener('orientationchange', schedule, {passive: true});
  window.addEventListener('pageshow', schedule);
  if (window.visualViewport) window.visualViewport.addEventListener('resize', schedule, {passive: true});
  document.addEventListener('visibilitychange', function () {
    if (!visible()) {
      if (poll !== null) window.clearTimeout(poll);
      if (pending !== null) window.clearTimeout(pending);
      poll = pending = null;
    } else { schedule(); armPoll(); }
  });
  // Preference is an invalidation signal ONLY. The decision always comes from
  // resolved ancestor colours and, when transparent, the actual UA Canvas.
  if (window.matchMedia) {
    var preference = window.matchMedia('(prefers-color-scheme: dark)');
    if (preference.addEventListener) preference.addEventListener('change', schedule);
    else if (preference.addListener) preference.addListener(schedule);
  }
  refresh();
})(window, document);
