# Create the Markdown Companion for SD6 Annexes

## Goal
Create `Md_subdocumento/LAFROX-Subdocumento6-Anexos.md` from the annex wrapper and `anexos.tex`, preserving the two annexes and their explanatory text. Reconcile the procurement table to the user's prior approved T-14 decision rather than copying its contradictory buyer/month-5 claims. Keep unverified receipt and commissioning dates unspecified.

## Scope
- Output: `Md_subdocumento/LAFROX-Subdocumento6-Anexos.md`.
- Read-only sources: `LAFROX-Subdocumento6-Anexos.tex` and `anexos.tex`.
- Preserve the wrapper's title/subtitle/form context, Anexo 6.A stakeholder table and analysis, and Anexo 6.B acquisitions table and analysis.
- Do not modify LaTeX, PDFs, other Markdown, or unrelated files. Do not commit.

## Decisions and safeguards
- In Anexo 6.B, CLIENTE purchases field equipment. LafroX purchases technical-room/rack/server/edge equipment; purchase order is in month 2 and installation in month 3. The technical room is received in month 4; this is not equipment receipt or commissioning. Do not assert dates for equipment technical receipt or commissioning.
- SOC service remains conditional on subcontracting and RT-11.17 is partial because the SOC location is undeclared; do not imply a signed contract or full compliance.
- Keep the remaining source row details, package identifiers, responsible roles, and evidence intact unless a detail would contradict these approved constraints.

## Tasks
1. [x] Convert the annex wrapper and both annex sections/tables/analysis into readable Markdown, including all 17 stakeholder rows and all 14 acquisition rows; apply the approved acquisition and SOC qualifications. Evidence: created `Md_subdocumento/LAFROX-Subdocumento6-Anexos.md` with metadata, both annexes, all source rows/analysis, T-14 buyer correction, distinct month-2 order/month-3 installation/month-4 room receipt, unspecified equipment receipt/commissioning, and conditional/partial SOC status.
2. [x] Verify row counts, source-detail parity, internal/cross-document links, the purchase milestones and SOC wording; run scoped whitespace/diff checks. Evidence: verifier confirmed 17 stakeholder rows and 14 procurement rows, source fields preserved, approved buyer/timing reconciliation and SOC qualification correct; relative link resolves; Python structure/whitespace check exited 0. No `git diff --check` claim because the new file is untracked.

## Evidence
- User chose “Alinear al criterio acordado” after the acquisition conflict in the source was surfaced.
