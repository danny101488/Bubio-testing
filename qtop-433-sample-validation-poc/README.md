# qtop #433 sample-validation CI proof

This is a small public proof packet for `qtop/qtop#433`.

It demonstrates the structure proposed for qtop:

- one shared `make sample-validation` entry point
- dependency-free Python validation
- bundled PBS, SGE, and Slurm sample fixtures
- deterministic rendered-output artifacts
- a machine-readable `manifest.json`
- GitHub Actions and GitLab CI jobs that call the same Makefile target

This repository is only a proof packet. The actual qtop patch was prepared against `qtop/qtop` on branch `codex/challenge-433-ci-samples`.

## Run

```bash
make sample-validation
```

Output is written to `build/sample-validation/`.

## Validation Performed

The local proof run completed with:

```text
python3 scripts/validate_sample_gate.py --output build/sample-validation
```

No dependency installs or package fetches are required.

Drafted with Codex / GPT-5.5 xHigh assistance and reviewed before public posting.
