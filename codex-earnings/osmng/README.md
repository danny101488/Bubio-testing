# OSM-NG patch artifacts

These patch files are temporary review artifacts for OpenStreetMap-NG bounty work prepared by Codex while the fork/PR path is being sorted.

They are not a substitute for proper pull requests. Each patch was generated from a clean local worktree and had `git diff --check` run locally. Full tests were not run because the local machine does not have the repo's required Python 3.14/Nix test environment installed, and dependency-fetching setup was intentionally avoided on this high-value machine.

Patch files:

- `osmng-126-close-notes.patch` for `openstreetmap-ng/openstreetmap-ng#126`
- `osmng-100-trace-recompress.patch` for `openstreetmap-ng/openstreetmap-ng#100`
- `osmng-31-avatar-error.patch` for `openstreetmap-ng/openstreetmap-ng#31`
