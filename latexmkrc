# latexmkrc -- clase lafrox
# LuaLaTeX obligatorio (fontspec + TikZ overlay en la portada).
$pdf_mode = 4;                      # 4 = lualatex
$lualatex = 'lualatex --interaction=nonstopmode --shell-escape --synctex=1 %O %S';
$bibtex_use = 2;
$biber = 'biber %O %B';             # solo se usa con la opcion de clase [apa]
$clean_ext = 'synctex.gz run.xml bbl bcf loc lol nav snm vrb';

# La foliación correlativa del sobre la calcula compilar_sobre1.py, que llama
# a latexmk documento por documento en el orden del índice A-5.
@default_files = ('LAFROX-Formulario-A-5.tex', 'LAFROX-Formulario-A-1.tex',
                  'LAFROX-Formulario-A-2.tex', 'LAFROX-Formulario-A-3.tex',
                  'LAFROX-Formulario-A-4.tex', 'LAFROX-Formulario-A-6.tex');
