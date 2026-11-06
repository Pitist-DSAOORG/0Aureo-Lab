from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import platform
import statistics
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "bench" / "results"
OUT.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("--cold-runs", type=int, default=3)
parser.add_argument("--warm-runs", type=int, default=5)
args = parser.parse_args()

if args.cold_runs < 1 or args.warm_runs < 1:
    raise SystemExit("Las ejecuciones deben ser >= 1")

report = {
    "schema": "0aureo-lean-benchmark-v1",
    "started_utc": datetime.now(timezone.utc).isoformat(),
    "environment": {
        "platform": platform.platform(),
        "python": sys.version,
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
    },
    "commit": subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT, capture_output=True, text=True
    ).stdout.strip(),
    "inputs_sha256": {},
    "cold": [],
    "warm": [],
    "status": "RUNNING",
}

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def execute(label, command):
    start = time.perf_counter()
    result = subprocess.run(
        command, cwd=ROOT, text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    elapsed = time.perf_counter() - start

    logfile = OUT / (label + ".log")
    logfile.write_text(result.stdout, encoding="utf-8")

    record = {
        "label": label,
        "command": command,
        "seconds": round(elapsed, 6),
        "returncode": result.returncode,
        "log": str(logfile.relative_to(ROOT)),
    }

    print(label, f"{elapsed:.3f}s", "exit=", result.returncode)

    if result.returncode:
        raise RuntimeError(f"{label} falló. Log: {logfile}")

    return record

def stats(records):
    values = [r["seconds"] for r in records]
    return {
        "runs": len(values),
        "median_seconds": statistics.median(values),
        "min_seconds": min(values),
        "max_seconds": max(values),
        "mean_seconds": statistics.mean(values),
        "stdev_seconds": (
            statistics.stdev(values) if len(values) > 1 else 0.0
        ),
    }

for name in [
    "lakefile.lean", "lean-toolchain",
    "Aureo/Basic.lean", "Aureo/PipelineTest.lean",
    "tests/lean/Regression.lean"
]:
    path = ROOT / name
    if path.is_file():
        report["inputs_sha256"][name] = digest(path)

try:
    execute("lean_version", ["lean", "--version"])
    execute("lake_version", ["lake", "--version"])

    for i in range(args.cold_runs):
        execute(f"cold_clean_{i+1}", ["lake", "clean"])
        report["cold"].append(
            execute(f"cold_build_{i+1}", ["lake", "build"])
        )

    for i in range(args.warm_runs):
        report["warm"].append(
            execute(f"warm_build_{i+1}", ["lake", "build"])
        )

    report["regression_compile"] = execute(
        "regression_compile",
        ["lake", "env", "lean", "tests/lean/Regression.lean"]
    )

    report["cold_summary"] = stats(report["cold"])
    report["warm_summary"] = stats(report["warm"])
    report["status"] = "PASS"

except Exception as exc:
    report["status"] = "FAIL"
    report["error"] = str(exc)
    raise

finally:
    report["finished_utc"] = datetime.now(timezone.utc).isoformat()
    destination = OUT / "benchmark.json"
    destination.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print("REPORT=", destination)
    print("STATUS=", report["status"])
