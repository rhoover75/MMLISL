// GRIT site — shared nav behavior (mobile menu + dropdown)
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".menu-toggle");
  var links = document.querySelector(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
    });
  }

  document.querySelectorAll(".has-dropdown > button.nav-link").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var parent = btn.closest(".has-dropdown");
      var wasOpen = parent.classList.contains("open");
      document.querySelectorAll(".has-dropdown.open").forEach(function (el) {
        el.classList.remove("open");
      });
      if (!wasOpen) parent.classList.add("open");
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-dropdown")) {
      document.querySelectorAll(".has-dropdown.open").forEach(function (el) {
        el.classList.remove("open");
      });
    }
    if (links && links.classList.contains("open") && !e.target.closest(".nav-pill")) {
      links.classList.remove("open");
    }
  });
});

// Critical Lifelines page — draw a connector showing the cybersecurity card
// feeding into all four lifeline cards above it.
//
// Two layouts, two different connector shapes:
//
// - Single row (desktop, 4 cards side by side): a short vertical arrow rises
//   from the cybersecurity card straight up into each card above it, in the
//   gap between the row and the card below. Nothing ever crosses a card, so
//   this is simple.
//
// - Stacked (narrower widths, cards in one column): a single vertical arrow
//   per card would either run straight through every card below it (if drawn
//   at each card's horizontal center) or, if hidden behind the opaque cards,
//   read as one card silently feeding the next rather than cybersecurity
//   reaching all four independently. Instead we draw a "rail": one vertical
//   trunk line down the right-hand side of the stack, in a strip of padding
//   reserved on every card (see `.lifeline-card, .cyber-card` padding-right
//   in the 980px breakpoint in styles.css) so it never crosses any text, with
//   a short horizontal branch — arrowhead included — poking left into each
//   lifeline card, and a plain stub showing the trunk emerging from the
//   cybersecurity card's own right edge.
(function () {
  var stack = document.querySelector(".lifeline-stack");
  if (!stack) return;

  var svg = stack.querySelector(".cyber-connectors");
  var cyberCard = stack.querySelector(".cyber-card");
  var cards = stack.querySelectorAll(".lifeline-card");
  if (!svg || !cyberCard || !cards.length) return;

  // SVG auto-orientation rotates a marker assuming it is drawn pointing
  // along +x (rightward) in its own local coordinates, then rotates that by
  // the line's tangent angle at the vertex it's attached to — so a triangle
  // authored pointing right will correctly become an "up" arrow on a
  // vertical line or a "left" arrow on a horizontal one, automatically.
  var MARKER_DEFS =
    '<defs><marker id="cyberArrow" viewBox="0 0 10 10" refX="9" refY="5" ' +
    'markerWidth="6" markerHeight="6" orient="auto">' +
    '<path d="M0,0 L10,5 L0,10 Z" fill="var(--gold-500)"/></marker></defs>';

  function drawRow(stackRect) {
    var cyberRect = cyberCard.getBoundingClientRect();
    var cyberTopY = cyberRect.top - stackRect.top;
    var markup = MARKER_DEFS;

    cards.forEach(function (card) {
      var r = card.getBoundingClientRect();
      var x = r.left + r.width / 2 - stackRect.left;
      var yTop = r.bottom - stackRect.top + 6;
      markup +=
        '<line x1="' + x + '" y1="' + cyberTopY + '" x2="' + x + '" y2="' + yTop +
        '" stroke="var(--gold-500)" stroke-width="2.5" stroke-linecap="round" ' +
        'marker-end="url(#cyberArrow)"/>';
    });

    return markup;
  }

  function drawStacked(stackRect) {
    var cyberRect = cyberCard.getBoundingClientRect();
    // The whole rail — trunk, branches, arrowheads — lives in the blank
    // gutter .lifeline-stack reserves to the right of the (now narrower)
    // cards (see the 980px breakpoint in styles.css). Nothing here should
    // ever be drawn at or past a card's own right edge: the rail sits near
    // the outer edge of the gutter, and branch tips stop a few px short of
    // each card, floating just outside it rather than touching or crossing
    // into it.
    var TRUNK_INSET = 14; // px from the stack's outer right edge — the vertical rail
    var TIP_GAP = 6; // px between an arrow tip and the card's own right edge
    var trunkX = stackRect.width - TRUNK_INSET;

    var branches = [];
    cards.forEach(function (card) {
      var r = card.getBoundingClientRect();
      branches.push({
        y: r.top - stackRect.top + r.height / 2,
        tipX: r.right - stackRect.left + TIP_GAP
      });
    });

    var cyberY = cyberRect.top - stackRect.top + cyberRect.height / 2;
    var cyberTipX = cyberRect.right - stackRect.left + TIP_GAP;

    var markup = MARKER_DEFS;

    // Trunk: one continuous rail from the topmost card's branch down to
    // where it meets the cybersecurity card.
    markup +=
      '<line x1="' + trunkX + '" y1="' + branches[0].y + '" x2="' + trunkX +
      '" y2="' + cyberY + '" stroke="var(--gold-500)" stroke-width="2.5" ' +
      'stroke-linecap="round"/>';

    // Branches into each lifeline card, arrowhead pointing into the card.
    branches.forEach(function (b) {
      markup +=
        '<line x1="' + trunkX + '" y1="' + b.y + '" x2="' + b.tipX + '" y2="' + b.y +
        '" stroke="var(--gold-500)" stroke-width="2.5" stroke-linecap="round" ' +
        'marker-end="url(#cyberArrow)"/>';
    });

    // Stub showing the trunk emerging from the cybersecurity card — the
    // source, so no arrowhead.
    markup +=
      '<line x1="' + trunkX + '" y1="' + cyberY + '" x2="' + cyberTipX + '" y2="' + cyberY +
      '" stroke="var(--gold-500)" stroke-width="2.5" stroke-linecap="round"/>';

    return markup;
  }

  function draw() {
    var stackRect = stack.getBoundingClientRect();

    svg.setAttribute("width", stackRect.width);
    svg.setAttribute("height", stackRect.height);
    svg.setAttribute("viewBox", "0 0 " + stackRect.width + " " + stackRect.height);

    var firstTop = cards[0].getBoundingClientRect().top;
    var lastTop = cards[cards.length - 1].getBoundingClientRect().top;
    var isSingleRow = Math.abs(firstTop - lastTop) < 2;

    svg.innerHTML = isSingleRow ? drawRow(stackRect) : drawStacked(stackRect);
  }

  window.addEventListener("load", draw);
  window.addEventListener("resize", function () {
    window.requestAnimationFrame(draw);
  });
  window.addEventListener("orientationchange", function () {
    window.requestAnimationFrame(draw);
  });
  // Fonts loading late can shift card heights slightly; redraw once settled.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(draw);
  }
  draw();
})();
