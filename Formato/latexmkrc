# latexmkrc -- clase lafrox
# LuaLaTeX obligatorio (fontspec + TikZ overlay en la portada).
$pdf_mode = 4;                      # 4 = lualatex
$lualatex = 'lualatex --interaction=nonstopmode --shell-escape --synctex=1 %O %S';
$bibtex_use = 2;
$biber = 'biber %O %B';             # solo se usa con la opcion de clase [apa]
$clean_ext = 'synctex.gz run.xml bbl bcf loc lol nav snm vrb';

# ---------------------------------------------------------------------------
#  SumatraPDF: auto-reload nativo + SyncTeX inverse search
#
#  - $pdf_previewer: abre SumatraPDF con forward search (va a la linea del .tex
#    que corresponde a la posicion actual del cursor).
#  - -inverse-search: doble clic en el PDF abre Antigravity IDE en la linea
#    exacta del .tex. Usa el CLI de Antigravity IDE (basado en VS Code --goto).
#  - $pdf_update_method = 0: deja que SumatraPDF detecte el cambio en disco
#    solo (lo hace nativamente, sin senal externa).
# ---------------------------------------------------------------------------
$pdf_previewer = '"C:/Users/henri/AppData/Local/SumatraPDF/SumatraPDF.exe" -reuse-instance -forward-search %S %L %D -inverse-search "\"C:/Users/henri/AppData/Local/Programs/Antigravity IDE/Antigravity IDE.exe\" --goto \"%%f:%%l\""';
$pdf_update_method = 0;
