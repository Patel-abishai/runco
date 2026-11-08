// run.co prototype router: one <section> per screen, hash routes (#Home, #Lobby ...)
(function () {
  var screens = Array.prototype.slice.call(document.querySelectorAll(".screen"));
  var ids = screens.map(function (s) { return s.id; });
  var first = ids[0];

  function show() {
    var id = decodeURIComponent(location.hash.slice(1)) || first;
    if (ids.indexOf(id) === -1) id = first;
    screens.forEach(function (s) {
      var on = s.id === id;
      s.hidden = !on;
      if (on) {
        var b = s.querySelector(".body");
        if (b) b.scrollTop = 0;
      }
    });
    document.querySelectorAll(".flow a").forEach(function (a) {
      if (a.getAttribute("href") === "#" + id) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    document.title = "run.co · " + id;
  }

  // Buttons inside forms should never reload the page
  document.addEventListener("submit", function (e) { e.preventDefault(); });

  window.addEventListener("hashchange", show);
  show();
})();
