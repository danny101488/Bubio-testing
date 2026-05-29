# Bitgesell #32 Repository Links Patch

Target issue: https://github.com/BitgesellOfficial/bitgesell/issues/32

This folder contains a small PR candidate for the Bitgesell PR bounty hunt. It updates stale repository references in Debian package metadata and Windows build documentation to the active official repository.

## Patch

- `0001-docs-refresh-repository-links.patch`

## Local source state

- Local repo: `/Users/danielcabezas/.codex/earnings-artifacts/round14/oss-work/bitgesell`
- Branch: `codex/refresh-repository-links`
- Commit: `4e68caf9b82c61c59a0b1b11679878aa5ee77267`

## Files changed

- `debian.minimal/control`
- `debian.minimal/copyright`
- `debian.qt/control`
- `doc/build-windows.md`

## Verification

- `git diff --check HEAD~1 HEAD`
- `rg -n "github.com/(wu-emma|Original-Tasty)/bitgesell" debian.minimal debian.qt doc/build-windows.md` returned no matches.

## Submission status

Not submitted upstream yet. This public proof packet exists because the current GitHub connector can write only to `danny101488/Bubio-testing`, and no writable fork of `BitgesellOfficial/bitgesell` was visible.
