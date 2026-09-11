/* drawer + active link + search */
(function () {
  var body = document.body;
  var ham = document.getElementById('hamburger');
  var scrim = document.getElementById('scrim');
  if (ham) ham.addEventListener('click', function () { body.classList.toggle('nav-open'); });
  if (scrim) scrim.addEventListener('click', function () { body.classList.remove('nav-open'); });
  document.querySelectorAll('.sidebar a').forEach(function (a) {
    a.addEventListener('click', function () { body.classList.remove('nav-open'); });
  });
  // active link
  var cur = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.sidebar a').forEach(function (a) {
    if (a.getAttribute('data-href') === cur) a.classList.add('active');
  });
  // search
  var box = document.getElementById('search'), res = document.getElementById('results'), idx = null;
  function hide() { if (res) res.style.display = 'none'; }
  document.addEventListener('click', function (e) {
    if (res && !document.querySelector('.searchwrap').contains(e.target)) hide();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hide(); });
  if (!box) return;
  fetch('assets/search-index.json').then(function (r) { return r.json(); })
    .then(function (j) { idx = j; }).catch(function () { idx = []; });
  box.addEventListener('input', function () {
    var q = box.value.trim().toLowerCase();
    if (!idx || q.length < 2) { hide(); return; }
    var words = q.split(/\s+/);
    var hits = idx.filter(function (e) {
      var t = e.t.toLowerCase();
      return words.every(function (w) { return t.indexOf(w) !== -1; });
    }).slice(0, 8);
    if (!hits.length) { hide(); return; }
    res.innerHTML = hits.map(function (e) { return '<a href="' + e.u + '">' + e.t + '</a>'; }).join('');
    res.style.display = 'block';
  });
})();
