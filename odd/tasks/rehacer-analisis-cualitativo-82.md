# Rework section 8.2.2 qualitative risk analysis

## Goal
Replace all of section 8.2.2 in `08_plan_riesgos/contenido.tex` with an introduction aligned to the updated T-16 risk register, a paginated table of all 45 risks, and a concise data-based interpretation.

## Authority and decisions
- User authorized redoing the whole section 8.2.2 based on updated risks in T-16.
- The table contains only: risk ID, probability, impact, exposure numeric value, and priority level.
- Use the current T-16 ordinal P/I values (do not import HH impact or old R8 FMEA/NPR values).
- Exposure is P × I. Priority mapping remains the SD8 matrix: 1–4 Baja, 5–9 Media, 10–16 Alta, 17–25 Crítica.
- Keep edits scoped to section 8.2.2 in `08_plan_riesgos/contenido.tex`; preserve other local changes and do not replace existing PDFs or create commits.
- This is a documentation rewrite, so no meaningful behavior-test RED applies; verify structure, calculation consistency, and LuaLaTeX build instead.

## Tasks
1. [x] Rewrite the section intro, five-column 45-risk table, and concise priority-distribution discussion from T-16.
2. [x] Verify table values/priority bands and compile to temporary output without replacing project PDFs.

## Sources
- T-16: `Lafrox-Subdocumento-T-16.tex:20,27–72`.
- SD8 priority matrix: `08_plan_riesgos/contenido.tex:80–91`.
- Rewritten subsection: `08_plan_riesgos/contenido.tex:125–179`.
- Prior ODD decisions/evidence: `odd/tasks/ajustar-tabla-t16-bases-administrativas.md`.

## Evidence
- The subsection is titled “Análisis cualitativo de riesgos” and the table contains exactly ID, ordinal probability, ordinal impact, exposure P×I, and priority level for R-001–R-045 in order.
- Verification compared every P/I/exposure/priority against T-16 and SD8 bands; distribution confirmed as 20 Baja, 23 Media, 2 Alta, 0 Crítica. The previous FMEA/NPR extract and legacy R8 references were removed from this subsection.
- `git diff --check` exited 0; only a Git LF→CRLF working-copy warning appeared for T-16 `.tex`.
- `latexmk -lualatex` succeeded in `/tmp/lafrox-sd8-qualitative-final` after three LuaLaTeX passes; PDF is 19 pages. Visual inspection of pages 12–14 showed the ID column stays on one line. The Exposición header wraps across lines.
- Native review: ASSESS returned unassessable because untracked task files lacked declaration; the separate verification plan was followed. The exact native reviewer approved; acknowledgement completed and authority was burned.
- Changes were limited to the intended subsection; no project PDF was replaced and no commit was created.
