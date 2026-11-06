# 0Aureo reproducible Lean benchmarks

Measures:
- Lean/Lake builds after lake clean.
- Repeated builds without cleaning.
- Direct compilation of the regression file.
- SHA-256 hashes of input files.
- Environment and toolchain versions.

Run:

    python bench/integrity.py
    lake update
    python bench/run.py --cold-runs 3 --warm-runs 5

Cold means project build-directory cleanup, not a guaranteed empty
operating-system or dependency cache.

These benchmarks measure Lean compilation, not AI inference speed.
