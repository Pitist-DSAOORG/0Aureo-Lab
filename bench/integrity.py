from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "lakefile.lean",
    "lean-toolchain",
    "Aureo/Basic.lean",
    "Aureo/PipelineTest.lean",
    "tests/lean/Regression.lean",
    "bench/integrity.py",
]

failed = False

for name in required:
    path = ROOT / name
    if not path.is_file():
        print("FAIL MISSING", name)
        failed = True
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print("PASS FILE", name, digest)

pattern = re.compile(r"\b(sorry|admit)\b")

for folder in ("Aureo", "tests/lean"):
    base = ROOT / folder
    if not base.exists():
        continue
    for path in sorted(base.rglob("*.lean")):
        content = path.read_text(encoding="utf-8")
        matches = pattern.findall(content)
        if matches:
            print("FAIL PLACEHOLDER", path, matches)
            failed = True
        else:
            print("PASS LEAN", path.relative_to(ROOT))

if failed:
    print("INTEGRITY=FAIL")
    sys.exit(1)

print("INTEGRITY=PASS")
