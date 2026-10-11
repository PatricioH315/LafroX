# Normalize T-16 risk statements

## Goal
Rewrite all 45 risk statements in the T-16 `Riesgo` column using the FEP04 cause–uncertain-event–effect structure while preserving the existing risk meaning and all other table fields.

## Authority and constraints
- User clarified that the target is T-16, not the official T-11 form.
- Target: `Lafrox-Subdocumento-T-16.tex`, table rows R-001–R-045.
- Use the proposed pattern: `Dado que <certain cause>, puede que <uncertain event>, teniendo como consecuencia <effect on a project objective>.`
- Preserve IDs, category, probability, impact, exposure, mitigation, owners, layout, and pre-existing unrelated local changes.
- Do not alter external CSVs or replace the local PDF. Do not create a commit.

## Tasks
1. [x] Normalize the 45 risk statements, retaining each row's specific cause, event, and objective-level effect.
2. [x] Verify the 45 IDs and unchanged non-risk cells; compile to a temporary output and inspect the resulting table.

## Evidence
- FEP04, slide 36, in `Datos externos/clases + pmbok/FEP04_Gestion_de_Riesgos_TIC_transcripcion.md`: cause/event/effect pattern and definitions.
- `Lafrox-Subdocumento-T-16.tex:28–72`: all 45 rows use `Dado que …, puede que …, teniendo como consecuencia …`.
- Read-only verification confirmed IDs R-001–R-045 are sequential and only risk-cell text differs; the other seven columns per row are unchanged.
- `git diff --check` exited 0. LuaLaTeX compiled in a fresh temporary directory (exit 0; PDF 23 pages). Non-blocking log warnings: `\\@parboxrestore`, `fvextra`/`csquotes` load order, rerun-suggested labels, and a fontspec SourceSerif4 Math note.
- No source CSV or local PDF was replaced and no commit was created.
- Implementation delegated first to `gentle-ai-worker`, which was unusable because its session lacked a file-editing tool; the orchestrator applied the bounded, verified transformation inline instead.
