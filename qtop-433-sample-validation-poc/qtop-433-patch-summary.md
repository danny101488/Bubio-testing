# qtop #433 local patch summary

Prepared local qtop patch:

- Repo: `qtop/qtop`
- Local branch: `codex/challenge-433-ci-samples`
- Local commit: `879258509838282cb86f3b4a3f5953ac80abd2dd`
- Files changed: 8
- Insertions: 580
- Deletions: 3

Patch summary:

- adds `make sample-validation`
- adds GitHub Actions and GitLab CI jobs
- preserves rendered sample outputs and `manifest.json` as artifacts
- adds a dependency-free Python sample gate
- pins GitHub Actions third-party actions to full commit SHAs
- adds `make fortifications`
- documents sample sources, artifacts, and failure policy

Local validation already performed in the qtop checkout:

- `python3 -m py_compile tools/fortify_diff.py tools/validate_sample_gate.py tools/validate_pbs_samples.py tools/validate_slurm_samples.py`
- `make fortifications`
- `git diff --check`
- `git diff --cached --check`
- Ruby `Psych.load_file` parsed `.github/workflows/sample-validation.yml` and `.gitlab-ci.yml`
- `python3 tools/validate_sample_gate.py --output /tmp/qtop-sample-validation-test --max-failures 0`
- `make sample-validation SAMPLE_OUTPUT_DIR=/tmp/qtop-sample-validation-staged`
- `make sample-validation SAMPLE_OUTPUT_DIR=/tmp/qtop-sample-validation-round54`
- `python3 tools/validate_slurm_samples.py tests/plugins/slurm_samples --output /tmp/qtop-slurm-rendered-second`

Not run locally:

- `pytest`, because this machine does not currently have pytest installed and no dependency install was performed.
- Python 3.6/RHEL8 execution, because no local Python 3.6/RHEL8 container runtime was available.

Drafted with Codex / GPT-5.5 xHigh assistance and reviewed before public posting.
