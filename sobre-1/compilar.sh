#!/usr/bin/env bash
# Builds every Sobre N. 1 document and then the master file.
# Usage (from the repo root):  bash sobre-1/compilar.sh [folder-filter]
set -u
here="$(cd "$(dirname "$0")" && pwd)"
fail=0
for tex in "$here"/[1-4]-*/*/LAFROX-*.tex; do
  case "$tex" in *"${1:-}"*) ;; *) continue ;; esac
  dir="$(dirname "$tex")"
  if (cd "$dir" && latexmk -r "$here/latexmkrc" -silent "$(basename "$tex")" >/dev/null 2>&1); then
    echo "OK    ${tex#$here/}"
  else
    echo "FAIL  ${tex#$here/}"; fail=1
  fi
done
if [ -z "${1:-}" ] && [ -f "$here/LAFROX-Sobre1.tex" ]; then
  (cd "$here" && latexmk -r "$here/latexmkrc" -silent LAFROX-Sobre1.tex >/dev/null 2>&1) \
    && echo "OK    LAFROX-Sobre1.tex" || { echo "FAIL  LAFROX-Sobre1.tex"; fail=1; }
fi
exit $fail
