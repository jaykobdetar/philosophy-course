#!/usr/bin/env python3
"""Build an explicitly filtered teaching package; never package the source collection."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
RULES = json.loads((ROOT / "data/distribution.json").read_text())


def selected():
    paths = {ROOT / name for name in RULES["files"]}
    for name in RULES["directories"]:
        paths.update(p for p in (ROOT / name).rglob("*") if p.is_file())
    forbidden = set(RULES["excluded_roots"])
    result = []
    for path in paths:
        rel = path.relative_to(ROOT)
        if "__pycache__" in rel.parts or path.suffix == ".pyc":
            continue
        if not path.is_file() or path.is_symlink() or rel.parts[0] in forbidden:
            raise ValueError(f"Unsafe or missing allowlist path: {rel}")
        result.append(path)
    return sorted(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="show allowlisted files without writing a package")
    args = parser.parse_args()
    files = selected()
    if args.list:
        for path in files:
            print(path.relative_to(ROOT))
        return
    out = ROOT / "dist/teaching-only.zip"
    out.parent.mkdir(exist_ok=True)
    with ZipFile(out, "w", ZIP_DEFLATED) as z:
        for path in files:
            z.write(path, path.relative_to(ROOT))
    print(out)
    print("Teaching-only package; inspect rights before sharing.")


if __name__ == "__main__":
    main()
