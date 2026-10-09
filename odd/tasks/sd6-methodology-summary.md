# Summarize SD6 Methodologies and Align Forms

## Goal

Make the Subdocument 6 introduction an evaluative summary of project management and software-development methodologies, while retaining the implementation-level detail in the corresponding T-9 and T-10 forms. Keep the Markdown source and assembled LaTeX consistent, and preserve contractual claims without conflating distinct thresholds or unverified facts.

## Scope

Follow-on consistency surface: `Md_subdocumento/LAFROX-Subdocumento6.md` and `subdocumento_6/contenido.tex` for updating only the T-9/T-10 AI-use declaration rows to reflect the detailed Markdown adaptation; do not change SD6's concise methodology prose.

- `Md_subdocument/LAFROX-Subdocument6.md`: concise chapter introduction and section/subsection summaries; remove duplicated detailed tables/procedures only where T-9/T-10 already carry the corresponding detailed material.
- `subdocumento_6/contenido.tex` and the imported fragments under `subdocumento_6/tablas/`: align the assembled deliverable with the approved Markdown summary; preserve cross-reference structure and class conventions.
- `LAFROX-Formulario-T-9.tex`: correct the opening typo/awkward framing only.
- `LAFROX-Formulario-T-10.tex`: correct the cover subtitle to identify software development methodology.
- `Md_subdocumento/LAFROX-Formulario-T-9.md` and `Md_subdocumento/LAFROX-Formulario-T-10.md`: expand the current correspondence/index Markdown into complete detailed form counterparts aligned with the respective LaTeX content, including tables, references, and AI-use declarations.
- Do not change unrelated files, user work, or `subdocumento_6/tablas/ejemplo_tabla.tex`. Do not claim cross-document facts as verified when their source documents are unavailable in the current worktree. Do not silently reconcile conflicting facts.

## Tasks

1. [x] Summarize the SD6 introduction and preserve accurate links to the two forms and referenced SDs. Evidence: updated Markdown and assembled LaTeX introductions with aligned PMBOK/earned-value/Kanban and RUP/DevSecOps summary; text review confirms both match. Cross-reference to SD4 retained; SD7 reference intentionally not asserted without source verification.
2. [x] Summarize 6.1 project-management methodology; retain its analysis and PMBOK/agile boundary. Evidence: concise PMBOK, baselines, earned-value, Kanban boundary, staged delivery and continuity summary aligned in Markdown and LaTeX.
3. [x] Summarize 6.1.1 stakeholders; keep the detailed register in T-9. Evidence: Markdown table removed and replaced with summary; LaTeX 6.1.1 aligned. LaTeX did not include a stakeholder table fragment, so no include was removed; shared fragment remains untouched.
4. [x] Summarize 6.1.2 communications; keep detailed recipients/cadences in T-9. Evidence: detailed SD6 matrix replaced with aligned Markdown/LaTeX summary; LaTeX table include removed only from SD6, shared fragment untouched.
5. [x] Summarize 6.1.3 and align acquisition responsibilities with the user's decision that T-14 is authoritative for the sala technical equipment purchase. Keep CLIENTE as purchaser of field equipment; assign sala/racks/servers/edge-equipment purchase to LafroX per T-14. Align the T-9 narrative and shared acquisition table as well as SD6; distinguish order, installation, technical equipment receipt, room receipt, and commissioning dates rather than collapsing them. Evidence: updated SD6 Markdown/LaTeX and T-9 prose/shared table per user's decision; month-2 order, month-3 installation, month-4 room receipt; equipment receipt/commissioning dates are not asserted.
6. [x] Summarize 6.1.4 integration and change control; preserve approval and acceptance distinctions. Evidence: aligned summary in Markdown/LaTeX preserves corrective-action vs formal change and acceptance evidence.
7. [x] Summarize 6.1.5 scope, schedule, and earned-value controls; retain only validated summary claims. Evidence: aligned Markdown/LaTeX summary retains baselines, traceability, earned-value assessment, escalation and separately authorized reserves; exact thresholds delegated to T-9.
8. [x] Summarize 6.1.6 decision mechanisms/governance; retain decision/escalation distinctions and reference T-9 for detail. Evidence: aligned summary replaces committee table/list and operating metrics; distinguishes weekly operational follow-up from formal committees and refers exact cadence/authority to T-9.
9. [x] Summarize 6.2 software-development methodology; retain RUP phase logic and distinguish iterations from formal acceptance/production. Evidence: RUP phases, incremental delivery, continuity and distinction from acceptance/march-white/production retained in aligned MD/TeX; T-12/T-10 references preserved.
10. [x] Summarize 6.2.1 architecture, refactoring, and technical debt; preserve SD4 reference without asserting unverified details. Evidence: aligned MD/TeX summary covers early validation, traceable evolution, test-preserved behavior, and impact/priority debt tracking; refers criteria to T-10.
11. [x] Summarize 6.2.2 DevSecOps, IaC, and automated tests; preserve the separate 70% RT-04.11 and 80% corporate modified-code coverage thresholds. Evidence: aligned Markdown/LaTeX summary retains distinct 70% business-logic coverage (RT-04.11) and 80% modified-code line coverage (LafroX policy), plus gates, traceable artifact promotion, IaC, reversible migrations; tooling/detail in T-10.
12. [x] Summarize 6.2.3 ceremonies/cadences/decisions without duplicating 6.2; preserve formal-change boundaries. Evidence: aligned summaries replace ceremony/artifact detail and retain increment-vs-delivery, architecture governance, and formal change distinctions; T-10 referenced for detail.
13. [x] Verify T-9/T-10 Markdown correspondence/indexes against the current detailed LaTeX forms; update only demonstrated mismatches. Evidence: current Markdown forms identify letters a/b and link to 6.1/6.2 with matching subsection maps; detailed LaTeX contents are present. No Markdown index mismatch found.
14. [x] Validate SD6 cross-references to SD4 and T-12/T-14/T-15 using available branch sources; document inaccessible or unresolved references rather than inventing validation. Evidence: read-only rama-md check supports SD4 architecture/CI, T-12 requirements traceability and T-15 planning/earned-value references; found T-14 vs T-9/SD6 purchaser contradiction and partial SOC claim (T-12 RT-11.17).
15. [x] Correct T-10 cover subtitle from “Solicitud de cambios” to software-development methodology. Evidence: `LAFROX-Formulario-T-10.tex` subtitle now reads “Metodología para el desarrollo de software”.
16. [x] Correct T-9 opening typo and revise its redundant/awkward sentence without changing commitments. Evidence: replaced malformed broad intro with a concise statement that T-9 develops SD6 §6.1 and its adapted PMBOK approach.
17. [x] Verify the summary keeps coverage thresholds distinct and describes RT-11.17/SOC as partial where T-12 says so. Keep the 70% RT-04.11 business-logic gate distinct from the 80% modified-code line-coverage policy. Since T-12 marks RT-11.17 partial due to the undeclared SOC location, qualify any SOC procurement/service mention in SD6/T-9 as conditional and not fully compliant/awarded; do not imply it is already contracted. Evidence: distinct thresholds read back in MD and LaTeX; SOC caveat appears in aligned §6.1.3 and shared acquisition row.

18. [x] Compile and structurally verify the SD6/T-9/T-10 LaTeX deliverables and inspect the scoped diff. Evidence: LuaLaTeX/latexmk builds passed for SD6 (9 pages), T-9 (13 pages), and T-10 (7 pages) into a temporary directory; PDF text checks passed for headings, summary/detail split, acquisition roles/timelines, SOC caveat, coverage thresholds, and form titles; `git diff --check` passed. Temp output: `C:\\Users\\maxim\\AppData\\Local\\Temp\\lafrox-sd6-9Jru0wXe`. Work remains uncommitted; no commit authorization was given.
19. [x] Expand `Md_subdocumento/LAFROX-Formulario-T-9.md` from an index into the full detailed management-methodology form, faithfully aligned with current T-9 LaTeX, including stakeholder, communications, and acquisition tables and the reconciled T-14/SOC caveats. Evidence: ported PMBOK/delivery plan, stakeholder register, communication/acquisition matrices, integration/change control, earned-value metrics, governance, references and AI disclosure; updated AI disclosure to include Markdown adaptation; purchaser roles/timing and SOC caveat retained.
20. [x] Expand `Md_subdocumento/LAFROX-Formulario-T-10.md` from an index into the full detailed software-development methodology form, faithfully aligned with current T-10 LaTeX and keeping the 70% and 80% coverage criteria distinct. Evidence: ported RUP phases/stages, architecture/debt, pipeline/tooling/gates, IaC/migrations/deploy windows, ceremonies/artifacts/decisions; preserved both separate coverage metrics, references, and AI declaration (updated for Markdown adaptation; review remains undocumented).
21. [x] Verify both Markdown forms against current LaTeX content, check Markdown structure/cross-links, and review diff/whitespace. Evidence: T-9/T-10 content, tables, coverage criteria, acquisition/SOC caveats and SD6 links checked. Initial verification found SD6 still labels T-9/T-10 as cover-only/low in its AI declaration despite the expanded Markdown forms.
22. [x] Align the SD6 Markdown and assembled LaTeX AI-use rows for T-9/T-10 with their newly expanded Markdown contents, without changing concise methodology summaries or asserting human review. Evidence: both declarations now describe cover plus Markdown adaptation of detailed methodology/tables, level Alto, review No documentada.
23. [x] Reverify AI-use declaration consistency across SD6/T-9/T-10 and run final Markdown structure/link/diff checks. Evidence: declarations consistently state high-level Markdown adaptation and human review not documented; T-9/T-10 links resolve to SD6; T-10 §4.2 correctly cites SD4; scoped `git diff --check` exited successfully with no whitespace errors (Git emitted LF-to-CRLF warnings for the two updated form Markdown files).

## Verification

- Compare the edited Markdown and assembled LaTeX section-by-section.
- Check all retained cross-references, table/form mappings, section numbering, and LaTeX fragment imports.
- Compile the LaTeX deliverable into a temporary output directory; inspect build exit status, warnings, section/table presence, and generated PDF text.
- Run `git diff --check` and review the scoped diff; do not commit unless the user explicitly authorizes committing.

## Evidence

- User authorized proceeding with the previously previewed summary and asked that its sections/subsections be tasks.
- Current T-9/T-10 LaTeX already includes substantive detailed methodology; new Markdown forms should faithfully mirror that content while SD6 remains a summary.
- Current SD6 LaTeX has an unfinished “Este capítulo” placeholder. Its opening and numbered summaries need alignment with the fuller Markdown source.
- Cross-document branch evidence previously found distinct 70% (T-12) and 80% (SD1/corporate policy) thresholds, acquisition timing distinctions, and partial SOC compliance in T-12. Reconfirm against source before retaining these claims.
- The first 18 source-change and verification tasks are complete. This follow-on expands T-9/T-10 Markdown forms as explicitly requested.
