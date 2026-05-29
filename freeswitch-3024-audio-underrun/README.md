# FreeSWITCH #3024 candidate patch

Public patch artifact for `signalwire/freeswitch#3024`.

Target issue:

- `[Bounty $200] mod_conference: Core of the conference mixer wrongly inserts silence packets which cause audio distortion`
- https://github.com/signalwire/freeswitch/issues/3024

Patch file:

- `0001-fix-mod-conference-conceal-short-audio-input-underruns.patch`

Summary:

- allocates and uses the existing `member->last_frame` buffer
- tracks `last_read` and bounded `holdover_frames`
- when the mixer sees a short input-buffer tick for an otherwise active member, reuses the previous complete frame for up to two mixer ticks instead of allowing generated silence into the mix
- resets holdover tracking when a real member frame is read

Local validation:

- `git diff --check`
- reviewed allocation behavior: `switch_core_alloc` zeroes pool memory, so the new counters begin at zero

Not run locally:

- full FreeSWITCH build/reproduction, because the sparse checkout lacks generated build headers such as `switch_am_config.h`

This is intentionally a candidate patch for reporter/maintainer reproduction testing against the 1 kHz-tone case.

Drafted with Codex / GPT-5.5 xHigh assistance and reviewed before public posting.
