# SD9 Quality Fix

## Goal
Fix Subdocument 9 review blockers in Markdown deliverables after the commission review, preserving branch Markdown-only rules.

## Scope
Allowed edit surfaces:
- `09_plan_calidad/LAFROX-Subdocumento9.md`
- `09_plan_calidad/LAFROX-Subdocumento9-Anexos.md`
- `09_plan_calidad/LAFROX-Formulario-T-13.md`
- `09_plan_calidad/LAFROX-Formulario-T-17.md`
- `compct/CONTEXTO_SESION.md`

Out of scope unless explicitly needed after verification:
- non-Markdown files, `.drawio`, `.xlsx`, PDF/LaTeX, generated binaries
- completing `[[REVISIÓN HUMANA]]` cells without a real human reviewer
- committing, pushing, or publishing

## Tasks
- [x] Patch SD9/T-13/anexos for remaining review contradictions that can be resolved in Markdown.
- [x] Verify hotspot searches against the review prompt findings.
- [ ] Record unresolved human-only blockers and update session context.

## Evidence
- Started on branch `rama-md`.
- Source review: `Revision/revision_comision_informe2_SD9_v3.md` and latest `compct/CONTEXTO_SESION.md`.
- Incident: a delegated writer accidentally emptied `09_plan_calidad/LAFROX-Subdocumento9.md`; restored immediately from `HEAD` before applying intended edits. Initial worktree was clean, so no user edits were lost.
- Changed Markdown only: `09_plan_calidad/LAFROX-Subdocumento9.md`, `09_plan_calidad/LAFROX-Subdocumento9-Anexos.md`, `09_plan_calidad/LAFROX-Formulario-T-13.md`.
- Verification: `git diff --check` passed for SD9 Markdown files and this task file.
- Hotspot search: no remaining `primer paso a Producción`, `Capítulo 11`, `Figura 7.4`, stale DR months `27, 33`/`26, 32`, or old ISO 25012 overclaim; `[[REVISIÓN HUMANA]]` remains as a human-only blocker.
