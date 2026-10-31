#!/usr/bin/env python3
"""Build the offline course browser from the authoritative Markdown packets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'course' / 'content.js'

class Linker(HTMLParser):
    def __init__(self, source, pages):
        super().__init__(convert_charrefs=False)
        self.source, self.pages, self.parts = source, pages, []

    def handle_starttag(self, tag, attrs):
        cooked = []
        for key, value in attrs:
            if key in ('href', 'src') and value:
                parsed = urlsplit(value)
                if not parsed.scheme and not value.startswith('//'):
                    if parsed.path:
                        target = (ROOT / self.source).parent.joinpath(unquote(parsed.path)).resolve()
                    else:
                        target = ROOT / self.source
                    if target.is_relative_to(ROOT):
                        rel = target.relative_to(ROOT).as_posix()
                        if key == 'href' and rel in self.pages:
                            value = '?page=' + rel + (('#' + parsed.fragment) if parsed.fragment else '')
                        elif parsed.path:
                            value = '../' + rel + (('#' + parsed.fragment) if parsed.fragment else '')
            cooked.append((key, value))
        from html import escape
        self.parts.append('<' + tag + ''.join(f' {k}="{escape(v or "", quote=True)}"' for k,v in cooked) + '>')

    def handle_endtag(self, tag): self.parts.append('</' + tag + '>')
    def handle_data(self, data): self.parts.append(data)
    def handle_entityref(self, name): self.parts.append('&' + name + ';')
    def handle_charref(self, name): self.parts.append('&#' + name + ';')

paths = sorted(list((ROOT / 'current').rglob('*.md')) + list((ROOT / 'instruction').rglob('*.md')))
keys = {p.relative_to(ROOT).as_posix() for p in paths}
entries = {}
for path in paths:
    key = path.relative_to(ROOT).as_posix()
    source = path.read_text()
    rendered = subprocess.run(['pandoc', '--from', 'gfm', '--to', 'html5', '--no-highlight'], input=source, text=True, capture_output=True, check=True).stdout
    linker = Linker(key, keys)
    linker.feed(rendered)
    heading = next((line.lstrip('# ').strip() for line in source.splitlines() if line.startswith('# ')), path.stem)
    entries[key] = {'title': heading, 'html': ''.join(linker.parts), 'text': re.sub(r'\s+', ' ', source)[:12000]}

courses = []
for line in (ROOT / 'instruction' / 'README.md').read_text().splitlines():
    m = re.match(r'^\| (C\d\d[A-D]?) \| \[([^]]+)\]\(([^)]+)\)', line)
    if not m: continue
    code, title, link = m.groups()
    path = (ROOT / 'instruction' / link).resolve().relative_to(ROOT).as_posix()
    module_root = (ROOT / path).parent
    modules = [p.relative_to(ROOT).as_posix() for p in sorted((module_root / 'modules').glob('*.md'))]
    sessions = [p.relative_to(ROOT).as_posix() for p in sorted((module_root / 'sessions').glob('*.md'))]
    track = ROOT / 'instruction' / 'course-13' / 'tracks' / (code.lower()[1:] + '.md')
    courses.append({'code':code, 'title':title, 'path':path, 'modules':modules, 'sessions':sessions, 'track': track.relative_to(ROOT).as_posix() if track.exists() else None})

payload = {'pages':entries, 'courses':courses}
OUT.write_text('window.COURSE_DATA=' + json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n')
print(f'Built {len(entries)} pages and {len(courses)} course tracks in {OUT.relative_to(ROOT)}')
