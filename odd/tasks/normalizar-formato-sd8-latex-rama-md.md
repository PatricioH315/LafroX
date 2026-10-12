# Normalize SD8 presentation in LaTeX and rama-md

## Objective
Apply the user's requested signature/footer, verified APA citations, clean lists, pagination, minimum type size, cross-format parity, and AI-use declaration to the current SD8 LaTeX sources and its Markdown versions on `rama-md`.

## Problem and rationale
The current SD8 LaTeX is the content canon (45 risks, Annexes 8.A–8.B), but existing Markdown on `rama-md` diverges. The current local signature footer lacks the requested representative label. Source/citation metadata and every rendered figure/table must be checked against actual repository sources before claiming the documents are clean or equivalent.

## Scope
- Current worktree LaTeX: `main.tex`, `08_plan_riesgos/contenido.tex`, `LafroX-Subdocumento-8-Anexos.tex`, `Lafrox-Subdocumento-T-16.tex`, and SD8-local signature support `sd8-comun.tex` as needed.
- Markdown on branch `rama-md`: SD8 body, annex, and T-16 Markdown files identified from that branch's tree; align their content with the current LaTeX canon.
- Check referenced source documents in Git branches and PDFs where available; use verified metadata/page locations only.
- Build only in an isolated disposable copy. Inspect all figures/tables and report their state individually.

## Constraints
- Preserve pre-existing working-tree changes and the external PNGs; do not edit image assets or unrelated files.
- Do not restore or overwrite the existing modified PDFs; no compilation in the original worktree.
- Do not create commits or push unless the user later requests it.
- Do not invent source metadata, page citations, names of actual human reviewers, or missing content. Leave unsupported attribution or reviewer fields explicitly pending.
- Preserve the adopted 45-risk / Annex 8.A–8.B LaTeX content canon and existing quantitative decisions.

## Tasks
1. [done] Verify branch Markdown scope, source metadata, page locations, layout/list/footer mechanisms, and the current figure/table inventory; record evidence and unresolved facts.
2. [in progress] Implement the approved presentation, citation, pagination, minimum-size, clean-list, and AI-declaration changes in LaTeX without altering substantive risk decisions.
3. [pending] Align the three SD8 Markdown documents on `rama-md` with the current LaTeX canon and verified wording/references.
4. [pending] Compile all deliverables only in an isolated copy; visually inspect every figure/table, covers, page footers, and landscape pages; report check outcomes and outstanding blockers.

## Acceptance criteria
- Every source claim is cited only to a verified source and location; unsupported claims remain unattributed or pending.
- Signature image, representative label, and folio appear on every required page, including landscape pages, without clipping or overlap.
- Lists are structurally clean, pagination and minimum font size meet the request, and tables/figures remain readable.
- Markdown content matches LaTeX substance: 45 risks and Annexes 8.A–8.B, without unsupported legacy sections.
- AI-use declarations accurately identify tools/purpose and do not invent completed human review.
- Temporary compilation reports no errors or warnings, and visual inspection is recorded per figure/table.
- No unrelated changes, image modifications, PDF overwrite, commit, or push.

## Progress and evidence
- User selected the current LaTeX (45 risks, Annexes 8.A–8.B) as the canon for `rama-md` Markdown.
- User authorized checking already-referenced ISO/PMBOK sources; unsupported scale claims must not be attributed.
- User selected a minimum type size of **9 pt for all content**, including tables, footnotes, and figure labels.
- Current branch is `Lafrox_Subdocumento_8_Latex_Nuevo`; `rama-md` exists locally and as `origin/rama-md`.
- Exact Markdown paths on `rama-md`: `08_plan_riesgos/LAFROX-Subdocumento8.md`, `08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md`, and `08_plan_riesgos/LAFROX-Formulario-T-16.md`. Existing `Md_documentos/` files are not substitutes for editing that branch.
- Current local changes include prior SD8 analysis, signatures, Markdown, task documents, and modified PDFs. Preserve all of them.
- SD13 reference footer includes a signature image, “Media firma: [representante]”, and folio; current SD8 footer in `sd8-comun.tex` has image and folio but no representative label. The Markdown branch already contains `FIRMA_Alex_Aravena_transparente.png` at its root, so no image changes or copies are needed.
- Confirmed stale references: the SD8 body refers to Annex 8.E (lines 31, 210, 212); T-16 refers to response cost-benefit Annex 8.C (`Lafrox-Subdocumento-T-16.tex:21`), but the current annex root contains only 8.A–8.B. The references in `rama-md` carry the same mismatch. The body has two tables numbered 8.5; the exposure scale reuses the impact table label, and the probability bands overlap at 70%.
- Verified internal locators on `rama-md`: SD1 Table 1.3 is staffing headcount, while Table 1.6 is project-role assignment and dedication (`01_presentacion_empresa/LAFROX-Subdocumento1.md:176,343–355`). SD4 §§4.1.4.4, 4.2.5.1, 4.3.2.4 and Annexes 4-G/4-I/4-W exist; SD6 §6.1.6 exists; SD13 states the month-22 operational handover at `13_innovaciones/LAFROX-Subdocumento13.md:178`. SD3 Annex 3.H/V-13 is a pending consultation, not a CLIENTE answer (`03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:562–584`). A read-only audit in the new linked worktree confirmed SD1 issue date 05 Oct 2026; SD5 and SD6 issue date 12 Oct 2026; titles and locators in each source. SD3, SD4 and SD13 issue dates remain unverified. The three SD8 Markdown files have no explicit issue date/version in their opening metadata. APA no-date suffixes must therefore be reconciled by title, and the T-16 Markdown reference list currently omits SD8 although its introduction cites it.
- Verified T-16 as an Administrative Bases form (`Datos externos/Bases/Bases_Administrativas.md:1743–1746`) and AI disclosure requirement as Art. 13.5 / Form A-6 (`:233,1467–1471`). No Aclaraciones file was found, so Aclaraciones §§7.2/11 remain unverified and must not be asserted. IEC 60812 is listed in the main references but has no in-text citation found.
- PMBOK transcription in `Datos externos/clases + pmbok/PMBOK6_Cap11_Gestion_de_los_Riesgos_transcripcion.md` records Table 11-1 at printed p. 407 and risk-audit/reserve-analysis material at p. 456. Table 11-1 is explicitly an example; its text says probability/impact scales are context-specific. It does not source the project’s numerical bands, so those must be labeled as project-defined/contextualized rather than attributed directly to PMI. The full Spanish title, author, publisher and 2017/6th-edition metadata are available in `Datos externos/clases + pmbok/Guia_del_PMBOK_sexta_edicion_espanol.md:1–2`; the original PDF is absent from the current tree, so exact wording/page locations rely on the repository transcription.
- Available Bases source identifies the T-16 form and AI disclosure at Administrative Bases §13.5; the existing Aclaraciones §7.2 and §11 references were not verified in the available source files. Do not repeat them without evidence. The ISO catalogue search result confirms the title/year but its official page fetch returned HTTP 403; cite the official catalogue URL and state this access limitation in review notes.
- Explorer inventoried current figures/tables and layout hazards: SD8 RBS figure; body Tables 8.1–8.5 plus reserves and AI table; annex 45 manual fiches plus two tables; T-16 45-row landscape table and AI table. Inspect every rendered item individually.
- `rama-md` contains the signature PNG at the repository root; Markdown has no pagination or page footer. User selected a signature-image and “Media firma: representante” block near the Markdown cover/title metadata; no folio or per-page repetition is applicable in Markdown.
- Current class/source uses 9 pt table/figure text and 9.5 pt body text, while smaller text definitions exist. User has specified a 9 pt minimum across all content.
- A linked worktree for `rama-md` was created at `../LafroX-rama-md` and registered with the session; its source files were not modified during inspection.
- Initial LaTeX writer pass changed the footer and three document sources; its scoped `git diff --check` passed. No build or PDF write occurred. Parent readback found a formula regression to correct (`P×I` must remain `q_P×q_I`) and APA author/date consistency still needed a follow-up pass.
- Follow-up writer restored `q_P×q_I` and separated Table 8.5 from Table 8.6. Parent readback found the first-use PMI abbreviation incomplete; a subsequent scoped edit now defines it correctly. Internal reference locators, no-date suffixes/order, and citation-entry correspondence still need final APA review. No build or PDF write occurred; Task 2 remains in progress.
- Native ASSESS after the writer returned failed as `unassessable` because untracked paths were not declared. RDD is on; its returned plan treats this as high risk and requires writer self-verification plus an independent verifier. The final isolated build/visual verification must be delegated independently.
- No isolated compilation or rendered inspection for this feature has yet been performed.

## Route and checks
- Task 1: delegated read-only explorer; evidence: path/line references and source/PDF page verification.
- Task 2: bounded `gentle-ai-worker` edits only the listed LaTeX sources; documentation/presentation change, no meaningful test-first RED. Worker performs source-level checks only; compilation and rendering belong to the independent verifier.
- Task 3: same single writer/work unit only if safe to include alongside Task 2; otherwise parent will create separate narrow work unit after re-scoping. Use isolated worktree for `rama-md`.
- Task 4: delegated `gentle-ai-verify`, read-only, with exact build/copy commands and visual inspection checklist.
- No commits or push per explicit user constraint.

## Next step
Finish the remaining APA corrections (internal reference locators/order and citation-entry correspondence), then align the three Markdown documents in the separate `rama-md` worktree. The chosen signature block is already resolved. Keep the RBS diagram font-size as an explicit verification blocker if it cannot be measured without editing the asset. After both formats are complete, delegate isolated-copy compilation and per-figure/table visual inspection to an independent verifier; do not write PDFs in the original workspace.
