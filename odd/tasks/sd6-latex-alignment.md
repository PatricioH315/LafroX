# Align SD6 LaTeX with Markdown

## Goal
Bring the assembled LaTeX Subdocument 6 in `subdocumento_6/` into substantive alignment with the current source of truth, `Md_subdocumento/LAFROX-Subdocumento6.md`, while preserving LafroX class conventions and the existing `\chapter` / `\parte{}` structure.

## Scope
- Update `subdocumento_6/contenido.tex` and the imported fragments `tablas/interesados.tex`, `tablas/comunicaciones.tex`, and `tablas/adquisiciones.tex`.
- Transfer the current SD6 chapter content and tables, including sections 6.1.5 and 6.1.6, detailed project controls/governance, the expanded RUP/architecture/DevSecOps material, references, and AI-use declaration.
- Keep `subdocumento_6/tablas/ejemplo_tabla.tex` out of scope because it is not imported by `contenido.tex`; do not change other current user work.
- Preserve content wording and commitments from the Markdown except for necessary LaTeX escaping/formatting. Do not silently resolve factual contradictions with other subdocuments.

## Tasks
1. [x] Reconcile project-management prose, sections 6.1.5–6.1.6, and the three imported tables against current Markdown. Evidence: aligned 6.1 prose; imported stakeholder and communications tables updated; acquisitions table contains all 14 source rows with a 3-column wrapped layout. Compilation remains in task 3.
2. [x] Reconcile software-development sections, references, and AI-use disclosure against current Markdown. Evidence: 6.2/6.2.1–6.2.3, references, and five-row AI declaration transferred; declaration uses class-native wrapped table layout. Compilation remains in task 3.
3. [x] Compile SD6 and verify section/table presence, labels, output structure, and repository diff; record evidence and any remaining limitations. Evidence: `latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir="C:/Users/maxim/AppData/Local/Temp/lafrox-sd6" main.tex` exited 0; produced 16-page PDF; no rerun warnings after third pass. PDF text contains all 6.1–6.1.6 and 6.2–6.2.3 headings, table captions, references, AI declaration, and expected values/toolchain (SPI/CPI, .90, 70%, 80%, SLSA 3, Terraform, two-week iterations). `git diff --check` had no findings, but source paths are untracked and therefore outside Git's diff check. Pre/post build `git status --short` matched. PDF output is outside repo. User visually inspected the generated PDF and confirmed it looks correct.

## Verification
- Compile using LuaLaTeX/latexmk into a temporary output directory, not the repository.
- Check generated PDF text for all numbered sections, table captions, references, and AI declaration; ensure no fatal errors or unresolved cross-references.
- Inspect `git diff --check` and scoped diff; do not modify or commit unrelated changes.

## Evidence
- Branch at start: `LafroX-Subdoc6-LateX`.
- Baseline latest commit: `3faaec7` (`correccion: readme.`).
- Existing user/worktree changes before this task include modified `main.tex`, deleted `subdocumento-ejemplo/*`, and untracked `.vscode/`, `.codegraph/`, form files/PDFs, `Md_subdocumento/`, and `subdocumento_6/`; preserve them.
- Validation command and output: `latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir="C:/Users/maxim/AppData/Local/Temp/lafrox-sd6" main.tex`; exit 0, 16 pages, no remaining rerun warning after final pass. `pdftotext -layout` confirmed headings, tables, references, AI declaration, and key numeric/toolchain commitments. `git diff --check` returned no findings but does not cover the untracked source paths. User visually inspected the generated PDF and confirmed it looks correct.
- No commit was made because the user did not authorize committing.
