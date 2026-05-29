#!/usr/bin/env python3
"""Dependency-free sample validation proof for qtop/qtop#433."""

import argparse
import hashlib
import json
from pathlib import Path


SAMPLE_ROOTS = [
    ("pbs", Path("samples/pbs")),
    ("sge", Path("samples/sge")),
    ("slurm", Path("samples/slurm")),
]


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_sample(scheduler, path):
    text = path.read_text(encoding="utf-8")
    nonempty = [line for line in text.splitlines() if line.strip()]
    if len(nonempty) < 2:
        raise ValueError("{} sample {} is too small".format(scheduler, path))
    return {
        "scheduler": scheduler,
        "source": str(path),
        "line_count": len(text.splitlines()),
        "nonempty_line_count": len(nonempty),
        "sha256": digest(text),
        "preview": nonempty[:3],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    manifest = []
    for scheduler, root in SAMPLE_ROOTS:
        if not root.is_dir():
            raise SystemExit("missing sample root: {}".format(root))
        scheduler_output = output / scheduler
        scheduler_output.mkdir(exist_ok=True)
        for sample in sorted(root.glob("*")):
            if not sample.is_file():
                continue
            rendered = render_sample(scheduler, sample)
            target = scheduler_output / (sample.stem + ".json")
            target.write_text(json.dumps(rendered, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            manifest.append(rendered)

    if not manifest:
        raise SystemExit("no samples rendered")

    (output / "manifest.json").write_text(
        json.dumps({"samples": manifest}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("rendered {} samples to {}".format(len(manifest), output))


if __name__ == "__main__":
    main()
