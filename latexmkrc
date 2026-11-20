# LuaLaTeX obligatorio para lafrox.cls.
$pdf_mode = 4;
$lualatex = 'lualatex --interaction=nonstopmode --synctex=1 %O %S';
$bibtex_use = 2;
$biber = 'biber %O %B'; # Se utiliza con la opción de clase [apa].
$clean_ext = 'synctex.gz run.xml bbl bcf loc lol nav snm vrb';
# Configurar el visor y las rutas personales en cada equipo.
