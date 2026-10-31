(() => {
  'use strict';
  const {pages, courses} = window.COURSE_DATA;
  const $ = id => document.getElementById(id);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const url = key => '?page=' + encodeURIComponent(key);
  const current = new URLSearchParams(location.search).get('page');
  const valid = current && Object.hasOwn(pages, current) ? current : null;
  const activeCourse = courses.find(c => valid && (valid === c.path || c.modules.includes(valid) || c.sessions.includes(valid) || valid === c.track)) || null;
  const bookmarkKey = 'philosophy-course-bookmark-v1';
  const saved = (() => { try { const x = localStorage.getItem(bookmarkKey); return x && Object.hasOwn(pages,x) ? x : null; } catch { return null; } })();
  const courseCode = c => c.code.replace(/^C/,'');
  $('course-nav').innerHTML = courses.map(c => `<a href="${url(c.path)}" class="${activeCourse?.code === c.code ? 'active':''}"><span class="course-code">${esc(courseCode(c))}</span><span>${esc(c.title)}</span></a>`).join('');
  $('menu').addEventListener('click', () => { const open = $('menu').getAttribute('aria-expanded') !== 'true'; $('menu').setAttribute('aria-expanded',String(open)); document.querySelector('.rail').classList.toggle('open',open); });
  const auditPath = c => { const local = c.path.replace('README.md','source-audit.md'); return Object.hasOwn(pages, local) ? local : c.path.replace(/\/[a-d]\/README\.md$/, '/source-audit.md'); };
  const storageNote = '<p>Your bookmark stays in this browser on this device. It does not mark work complete or record assessment evidence.</p>';
  function home() {
    $('location').textContent = 'OVERVIEW';
    $('view').innerHTML = `<div class="page"><div class="eyebrow">A COURSE IN PHILOSOPHY · 14 COURSES</div><section class="hero"><div><h1>Think carefully.<br>Write clearly.</h1><p class="lead">Start with a text and a question. Follow the teaching packets through logic, history, ethics, knowledge, and independent research.</p><a class="primary" href="${url('instruction/course-01/sessions/01.md')}">Begin Session 1 <span aria-hidden="true">→</span></a>${saved ? `<a class="secondary" href="${url(saved)}">Return to bookmark</a>` : ''}</div><div class="hero-card"><div class="eyebrow">YOUR FIRST SESSION</div><div class="num">01</div><strong>First encounter with a philosophical text</strong><div class="rule"></div><p>Read OpenStax and Plato’s <em>Euthyphro</em>. Write a short paraphrase, keep your first attempt, and note one question.</p><p>About 90 minutes · No background required</p></div></section><div class="section-head"><h2>Explore the course</h2><small>Choose one option in Courses 11, 12 and 13</small></div><div class="course-grid">${courses.map(c => `<a class="card" href="${url(c.path)}"><span class="kicker">COURSE ${esc(courseCode(c))}</span><h3>${esc(c.title)}</h3><span class="meta">${c.modules.length} modules${c.sessions.length ? ` · ${c.sessions.length} opening sessions` : ''} <span aria-hidden="true">↗</span></span></a>`).join('')}</div><div class="note"><strong>Before reading-dependent work:</strong> check the source audit linked from each course. Some readings require online or library access. This course has authored teaching materials, but no learner pilot, human expert validation, or external credit. <a href="${url('instruction/source-status.md')}">View source status</a>.</div></div>`;
  }
  function reader(key) {
    const page = pages[key];
    const sequence = activeCourse ? [...activeCourse.sessions, activeCourse.path, ...(activeCourse.track ? [activeCourse.track] : []), ...activeCourse.modules] : [];
    const index = sequence.indexOf(key);
    const neighbors = index >= 0 ? `<div class="side-box"><h3>CONTINUE</h3>${index > 0 ? `<a href="${url(sequence[index-1])}">← Previous packet</a>` : ''}${index < sequence.length-1 ? `<a href="${url(sequence[index+1])}">Next packet →</a>` : ''}</div>` : '';
    const toc = activeCourse ? `<div class="side-box"><h3>${esc(activeCourse.code)} PACKETS</h3>${activeCourse.sessions.map((p,i) => `<a class="${key===p?'active':''}" href="${url(p)}">Opening session ${i+1}</a>`).join('')}<a class="${key===activeCourse.path?'active':''}" href="${url(activeCourse.path)}">Course guide</a>${activeCourse.track ? `<a class="${key===activeCourse.track?'active':''}" href="${url(activeCourse.track)}">Selected route</a>`:''}${activeCourse.modules.map((p,i) => `<a class="${key===p?'active':''}" href="${url(p)}">Module ${String(i+1).padStart(2,'0')}</a>`).join('')}</div>` : '';
    $('location').textContent = activeCourse ? activeCourse.code : 'REFERENCE';
    $('view').innerHTML = `<div class="page"><div class="crumb"><a href="index.html">Study desk</a> ${activeCourse ? ` / <a href="${url(activeCourse.path)}">${esc(activeCourse.code)} ${esc(activeCourse.title)}</a>` : ' / Reference'}</div><div class="reader-layout"><div class="reader"><div class="eyebrow">${activeCourse ? esc(activeCourse.code) + ' · TEACHING MATERIAL' : 'COURSE REFERENCE'}</div><div class="reader-sub">Current curriculum · Original packet preserved in Markdown</div><article class="prose">${page.html}</article></div><aside class="reader-side" aria-label="Reading tools"><div class="side-box"><h3>YOUR PLACE</h3><button id="bookmark">${saved === key ? 'Bookmarked ✓' : 'Bookmark this page'}</button>${saved && saved !== key ? `<a href="${url(saved)}">Open saved page →</a>` : ''}${saved ? '<button id="clear-bookmark">Clear bookmark</button>' : ''}${storageNote}</div>${neighbors}${toc}<div class="side-box"><h3>SOURCE FILE</h3><a href="../${esc(key)}">Open Markdown source ↗</a>${activeCourse ? `<a href="${url(auditPath(activeCourse))}">Source audit ↗</a>`:''}</div></aside></div></div>`;
    $('bookmark').addEventListener('click', () => { try { localStorage.setItem(bookmarkKey,key); location.reload(); } catch { alert('This browser did not allow local bookmark storage.'); } });
    $('clear-bookmark')?.addEventListener('click', () => { try { localStorage.removeItem(bookmarkKey); location.reload(); } catch {} });
    if (location.hash) requestAnimationFrame(() => document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView());
  }
  function search(q) {
    $('location').textContent = 'SEARCH';
    const words = q.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const results = words.length ? Object.entries(pages).map(([key,p]) => ({key,p,score:words.reduce((n,w) => n + (p.title.toLowerCase().includes(w) ? 8 : 0) + (p.text.toLowerCase().includes(w) ? 1 : 0),0)})).filter(x => words.every(w => x.p.title.toLowerCase().includes(w) || x.p.text.toLowerCase().includes(w))).sort((a,b) => b.score-a.score).slice(0,40) : [];
    $('view').innerHTML = `<div class="page"><div class="eyebrow">COURSE LIBRARY</div><h1>Search</h1><p class="lead">${results.length} result${results.length===1?'':'s'} for “${esc(q)}”</p>${results.map(({key,p}) => `<div class="search-result"><a href="${url(key)}">${esc(p.title)}</a><p>${esc(key)}</p></div>`).join('') || '<p>Try a course, author, topic, or packet ID.</p>'}</div>`;
  }
  const input = $('search');
  let timer;
  input.addEventListener('input', () => { clearTimeout(timer); timer=setTimeout(() => { if (input.value.trim()) search(input.value); else if (valid) reader(valid); else home(); },180); });
  document.addEventListener('keydown', e => { if (e.key === '/' && document.activeElement !== input && !['INPUT','TEXTAREA'].includes(document.activeElement.tagName)) { e.preventDefault(); input.focus(); } if(e.key==='Escape') input.blur(); });
  if (valid) reader(valid); else home();
})();
