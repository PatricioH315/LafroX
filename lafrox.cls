%% ============================================================================
%%  lafrox.cls -- Clase corporativa LafroX
%%  Propuestas tecnicas para la Licitacion N. TFEP-01/2026
%%  Caso 02 - Logistica (Distribuidora Puelche S.A.)
%%
%%  Motor: LuaLaTeX (obligatorio -- usa fontspec)
%%  Compilar: latexmk demo.tex     (el latexmkrc ya fija lualatex)
%%
%%  Tema: minimalista. Source Serif 4 en el cuerpo y Source Sans 3 en titulares,
%%  sin rellenos de color en las tablas y sin filas cebra (las filas se
%%  separan con filetes finos). El
%%  unico elemento expresivo es la caratula, que conserva la banda diagonal
%%  reducida a cabecera (v2.2): el tercio inferior queda en blanco porque es
%%  zona de firma y de folio, no zona de arte.
%%
%%  Cumplimiento formal cableado en la clase (Bases Administrativas, Art. 40):
%%    40.1  Foliacion correlativa, sin saltos, extremo inferior derecho
%%    40.2  Zona de media firma en el extremo inferior derecho de cada pagina
%%    40.3  Hoja resumen con folio inicial por seccion
%%    40.4  Carta u oficio vertical; cuerpo >= 11 pt; tablas y figuras >= 9 pt
%% ============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lafrox}[2026/09/17 v2.2 Clase corporativa LafroX, tema minimalista]

% ---------------------------------------------------------------------------
%  1. OPCIONES DE CLASE
% ---------------------------------------------------------------------------
\RequirePackage{iftex}

\newif\ifLFX@borrador   \LFX@borradorfalse
\newif\ifLFX@firma      \LFX@firmatrue
\newif\ifLFX@oficio     \LFX@oficiofalse
\newif\ifLFX@apa        \LFX@apafalse
\newif\ifLFX@notas      \LFX@notastrue

\DeclareOption{borrador}{\LFX@borradortrue}
\DeclareOption{final}{\LFX@borradorfalse\LFX@notasfalse}
\DeclareOption{firma}{\LFX@firmatrue}
\DeclareOption{sinfirma}{\LFX@firmafalse}
\DeclareOption{carta}{\LFX@oficiofalse}
\DeclareOption{oficio}{\LFX@oficiotrue}
\DeclareOption{apa}{\LFX@apatrue}
\DeclareOption{sinnotas}{\LFX@notasfalse}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ExecuteOptions{carta,firma}
\ProcessOptions\relax

\LoadClass[11pt,oneside,openany]{report}

\ifLuaTeX\else
  \ClassError{lafrox}{Esta clase requiere LuaLaTeX}{Compila con: latexmk demo.tex}
\fi

% ---------------------------------------------------------------------------
%  2. GEOMETRIA  (Art. 40.4: carta u oficio, orientacion vertical)
%
%  Margenes anchos y medida de linea corta: en un tema minimalista el aire es
%  el recurso principal, no los filetes.
% ---------------------------------------------------------------------------
\RequirePackage{geometry}
\ifLFX@oficio
  \geometry{paperwidth=8.5in,paperheight=13in}
\else
  \geometry{letterpaper}
\fi
%  headheight tiene que caber el texto del encabezado MAS el filete y su
%  separacion; con 14 pt fancyhdr avisaba "\headheight is too small" y la caja
%  del encabezado se desbordaba hacia el cuerpo, corriendo todo el bloque.
%  Si se cambia \LFXchico o \headrule, hay que revisar este valor: fancyhdr
%  dice en el log el minimo exacto que necesita.
%  footskip tiene que caber las tres filas del pie derecho (filete de firma,
%  rotulo y folio). Con 1,5 cm fancyhdr pedia al menos 46,8 pt; 52 pt deja
%  holgura para que un cambio menor de cuerpo no vuelva a dispararlo.
\geometry{top=2.9cm,bottom=3.0cm,left=3.1cm,right=2.7cm,
          headheight=27pt,headsep=16pt,footskip=52pt}

% ---------------------------------------------------------------------------
%  3. PALETA
%
%  Monocroma estricta: negro y grises neutros, sin matiz. No hay violeta, oro
%  ni azul, y tampoco colores semanticos de severidad o de estado. En un
%  documento de licitacion esas distinciones van en palabras y en columnas de
%  tabla, no en color.
%
%  Los grises son neutros de verdad (R=G=B): el gris anterior tiraba a azul y
%  se leia como color, no como tinta rebajada.
% ---------------------------------------------------------------------------
\RequirePackage[table,dvipsnames]{xcolor}

\definecolor{lafroxTinta}  {HTML}{111111}  % cuerpo de texto
\definecolor{lafroxFuerte} {HTML}{000000}  % titulares y numeracion
\definecolor{lafroxGris}   {HTML}{5F5F5F}  % texto secundario sobre claro
\definecolor{lafroxLinea}  {HTML}{C7C7C7}  % filetes de tabla
\definecolor{lafroxTenue}  {HTML}{DCDCDC}  % filetes de encabezado y pie
%  RESERVADO, sin uso desde la v2.2: la caratula ya no lleva fondo, es papel
%  blanco. Se conserva por si un anexo necesita una zona tramada.
\definecolor{lafroxBg}     {HTML}{F4F4F4}
%  Escalones de la banda de cabecera, de dentro hacia fuera. Sobre ellos el
%  texto va en blanco o en \lafroxSobre: es el unico lugar del documento
%  donde la tinta se invierte.
\definecolor{lafroxBanda}  {HTML}{141414}  % banda principal
\definecolor{lafroxBandaB} {HTML}{3C3C3C}  % diagonal de profundidad, interior
\definecolor{lafroxBandaC} {HTML}{606060}  % diagonal de profundidad, exterior
\definecolor{lafroxSobre}  {HTML}{9A9A9A}  % texto secundario sobre la banda
%  Acento de marca: filos de la banda de portada y cuna del pie de cada hoja.
\definecolor{lafroxNaranja} {HTML}{E8641B}  % acento, filo interior
\definecolor{lafroxNaranjaC}{HTML}{F29A5E}  % acento, filo exterior

% ---------------------------------------------------------------------------
%  4. TIPOGRAFIA
%
%  Pareja de la familia Source de Adobe (SIL OFL, incluida en MiKTeX/TeX Live):
%   - Source Serif 4 para el cuerpo y las tablas: con serif se lee mejor en
%     impresion y en paginas densas, que es como la comision lee la oferta.
%   - Source Sans 3 para titulares, rotulos, encabezado, pie y caratula
%     (\intermedium, \intersemibold y \sffamily).
%  Los nombres \intermedium/\intersemibold vienen de la version con Inter y se
%  conservan para no tocar cada titular de la clase.
%
%  El cuerpo queda en 11 pt, que es el minimo del Art. 40.4. No bajarlo.
% ---------------------------------------------------------------------------
\RequirePackage{fontspec}
\setmainfont{SourceSerif4}[Extension=.otf,
  UprightFont=*-Regular, ItalicFont=*-RegularIt,
  BoldFont=*-Semibold,   BoldItalicFont=*-SemiboldIt]
\setsansfont{SourceSans3}[Extension=.otf,
  UprightFont=*-Regular, ItalicFont=*-RegularIt,
  BoldFont=*-Semibold,   BoldItalicFont=*-SemiboldIt]
\newfontfamily\LFXsansmedio{SourceSans3}[Extension=.otf,
  UprightFont=*-Medium, ItalicFont=*-MediumIt]
\newfontfamily\LFXsansfuerte{SourceSans3}[Extension=.otf,
  UprightFont=*-Semibold, ItalicFont=*-SemiboldIt]
%  IBM Plex Mono para \texttt: rutas de planilla, opciones de clase y codigos.
\RequirePackage[scale=0.92]{plex-mono}

%  Matematica: STIX Two para lo que la fuente de texto no tiene, pero cifras,
%  letras y los simbolos que aparecen en tablas (< > = + - <= >= +- x %) se
%  toman de Source Serif 4. Asi "$\ge 95,0\%$" se ve igual que el texto que lo
%  rodea y no en otra fuente.
\RequirePackage{unicode-math}
\setmathfont{STIXTwoMath-Regular.otf}
\setmathfont{SourceSerif4-Regular.otf}[range={up/num,up/latin,up/Latin,
  "25,"2B,"3C,"3D,"3E,"B1,"D7,"2212,"2264,"2265}]
%  Coma decimal en modo matematico sin espacio detras ($95,0$ y no $95, 0$).
\RequirePackage{icomma}
\RequirePackage{microtype}

\newcommand{\interthin}{\normalfont}
\newcommand{\interlight}{\normalfont}
\newcommand{\intermedium}{\LFXsansmedio}
\newcommand{\intersemibold}{\LFXsansfuerte}

\RequirePackage[spanish,es-tabla,es-noquoting,es-nolists]{babel}
\RequirePackage{csquotes}

%  Interlineado: 1,10 (antes 1,18). Con Source Serif 4, de altura de x menor
%  que Inter, 1,18 dejaba las lineas visiblemente separadas. Las Bases no
%  fijan interlineado; solo el cuerpo minimo (Art. 40.4).
\linespread{1.10}
\setlength{\parskip}{0pt plus 2pt}
\setlength{\parindent}{1.5em}
\setlength{\emergencystretch}{2em}

% Cuerpos minimos exigidos por las Bases. No bajar de aqui.
%  En tabla se fuerzan cifras de ancho fijo: las columnas de codigos y de
%  cantidades tienen que alinearse verticalmente.
\newcommand{\LFXcuerpotabla}{%
  \fontsize{9.5pt}{12.5pt}\selectfont
  \addfontfeature{}}
\newcommand{\LFXcuerpofigura}{\fontsize{9pt}{11.5pt}\selectfont}

% Rotulo pequeno en mayusculas con interletraje abierto. Es el unico recurso
% "grafico" que se permite en los titulares del tema minimalista.
\newcommand{\LFXrotulo}[1]{%
  {\fontsize{7.5pt}{9pt}\selectfont
   \addfontfeature{}\intermedium
   \MakeUppercase{#1}}}

% ---------------------------------------------------------------------------
%  5. PAQUETES DE COMPOSICION
%
%  No se carga tcolorbox: en este tema no queda ninguna caja con relleno.
% ---------------------------------------------------------------------------
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{calc,positioning}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{xltabular}
\RequirePackage{array}
\RequirePackage{multirow}
\RequirePackage{makecell}
\RequirePackage{enumitem}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{fancyhdr}
\RequirePackage{caption}
\RequirePackage{pdflscape}
\RequirePackage{eso-pic}

% ---------------------------------------------------------------------------
%  Filetes entre filas
%
%  Toda tabla de la propuesta separa sus filas de datos con un filete fino en
%  lafroxLinea, sin que el autor escriba nada:
%   - tablalafrox: el filete se inserta en el cuerpo, tras cada \\ que no
%     vaya seguido ya de un filete (\midrule, \bottomrule, \hline, \cmidrule)
%     ni cierre la tabla.
%   - tabularx/tabular escritas a mano que abren con \toprule: \toprule deja
%     activo un \everycr que, tras cada fin de fila, mira el token siguiente y
%     dibuja el filete solo si viene otra fila de datos.
%  Para suprimirlo en una fila puntual: \LFXsinfilete al inicio de la fila
%  siguiente.
% ---------------------------------------------------------------------------
\newcommand{\LFXfiletefila}{%
  \noalign{{\color{lafroxLinea}\hrule height 0.3pt}\penalty\z@}}
%  El \penalty es imprescindible: tras un \hrule TeX no pone interlineado,
%  asi que sin el no quedaria ningun punto de corte entre filas y una tabla
%  larga no podria partirse de pagina.
\ExplSyntaxOn
\cs_new_protected:Npn \LFXsinfilete {}
\tl_new:N \l__lfx_cuerpo_tl
% Cuerpo de tablalafrox con filetes insertados.
\cs_new_protected:Npn \__lfx_filetear:n #1
  {
    \tl_set:Nn \l__lfx_cuerpo_tl {#1}
    \regex_replace_all:nnN
      { \c{\\} ( \[ [^\]]* \] )? }
      { \c{\\} \1 \c{LFXfiletefila} }
      \l__lfx_cuerpo_tl
    \regex_replace_all:nnN
      { \c{LFXfiletefila} ( \s* ) ( \c{midrule} | \c{bottomrule} | \c{hline}
                                  | \c{cmidrule} | \c{LFXsinfilete} | \Z ) }
      { \1 \2 }
      \l__lfx_cuerpo_tl
  }
\cs_new_eq:NN \LFXfiletear \__lfx_filetear:n
% \LFXconcuerpo{<apertura de xltabular y cabeceras>}: escribe la apertura,
% el cuerpo con filetes y el cierre \end{xltabular}.
\cs_new_protected:Npn \__lfx_concuerpo:nn #1#2 { #1 #2 \end{xltabular} }
\cs_new_protected:Npn \LFXconcuerpo #1
  { \exp_args:NnV \__lfx_concuerpo:nn {#1} \l__lfx_cuerpo_tl }
% Tablas escritas a mano: \everycr activado por \toprule.
\tl_new:N \l__lfx_filete_str
\cs_new_protected:Npn \__lfx_filete_mirar:
  { \futurelet \l__lfx_filete_sig_token \__lfx_filete_decidir: }
\cs_new_protected:Npn \__lfx_filete_decidir:
  {
    \bool_set_true:N \l_tmpa_bool
    \str_set:Nx \l__lfx_filete_str
      { \token_to_meaning:N \l__lfx_filete_sig_token }
    \regex_match:nVT
      { \A(?: \\noalign | end-group | \\crcr | \\cr\Z
            | (?:\\protected\ )?macro:->\\(?:noalign|LT|tbl_|crcr|endarray) ) }
      \l__lfx_filete_str
      { \bool_set_false:N \l_tmpa_bool }
    \clist_map_inline:nn
      { \bottomrule, \midrule, \toprule, \hline, \cmidrule, \end, \crcr,
        \egroup, \LFXsinfilete }
      {
        \token_if_eq_meaning:NNT ##1 \l__lfx_filete_sig_token
          { \bool_set_false:N \l_tmpa_bool }
      }
    \bool_if:NT \l_tmpa_bool
      { { \color{lafroxLinea} \hrule height 0.3pt } \penalty \c_zero_int }
    \egroup
  }
\cs_generate_variant:Nn \regex_match:nnT { nV }
\cs_new_eq:NN \LFXtopruleoriginal \toprule
\cs_set:Npn \toprule
  {
    \noalign { \global \everycr { \noalign \bgroup \__lfx_filete_mirar: } }
    \LFXtopruleoriginal
  }
% Al cerrar la tabla se apaga el \everycr: el pie de pagina y cualquier
% tabla posterior sin \toprule no deben heredar los filetes.
\clist_map_inline:nn { tabular, tabularx }
  { \AtEndEnvironment {#1} { \global \everycr { } } }
\ExplSyntaxOff
\RequirePackage{ragged2e}
%  lastpage: el total de folios del bloque de control documental de la
%  portada. El Art. 40.1 hace excluyente la foliacion, y declarar el total en
%  la caratula permite al evaluador detectar de inmediato un PDF truncado.
\RequirePackage{lastpage}

% Listas: tres niveles, marcas discretas en gris, sangria regular.
\setlist{itemsep=3pt,topsep=6pt,parsep=0pt}
\setlist[itemize,1]{leftmargin=1.5em,label=\textcolor{lafroxGris}{\textbullet}}
\setlist[itemize,2]{leftmargin=1.4em,label=\textcolor{lafroxGris!75}{\textendash}}
\setlist[itemize,3]{leftmargin=1.3em,label=\textcolor{lafroxGris!70}{\textbullet}}
\setlist[enumerate,1]{leftmargin=2.0em,label=\intermedium\arabic*.}
\setlist[enumerate,2]{leftmargin=1.9em,label=\textcolor{lafroxGris}{\alph*)}}
\setlist[enumerate,3]{leftmargin=2.0em,label=\textcolor{lafroxGris}{\roman*.}}
\setlist[description]{leftmargin=1.5em,itemsep=4pt,topsep=6pt,
                      font=\intersemibold\color{lafroxTinta}}

\AtBeginDocument{\color{lafroxTinta}}

% ---------------------------------------------------------------------------
%  6. METADATOS DE LA OFERTA
%     Se fijan con \datoslafrox{clave=valor, ...} en el preambulo.
% ---------------------------------------------------------------------------
\pgfkeys{
  /lafrox/.cd,
  empresa/.store in        = \LFXempresa,
  rut/.store in            = \LFXrut,
  representante/.store in  = \LFXrepresentante,
  cargo/.store in          = \LFXcargo,
  cliente/.store in        = \LFXcliente,
  licitacion/.store in     = \LFXlicitacion,
  caso/.store in           = \LFXcaso,
  documento/.store in      = \LFXdocumento,
  subtitulo/.store in      = \LFXsubtitulo,
  alcance/.store in        = \LFXalcance,
  formulario/.store in     = \LFXformulario,
  fecha/.store in          = \LFXfecha,
  version/.store in        = \LFXversion,
  logo/.store in           = \LFXlogo,
  %  Claves exigidas por el Art. 49.1 (bloque que debe leerse en la caratula)
  %  y por los Arts. 39 y 50.3. Sin ellas la portada no identifica la oferta.
  objeto/.store in         = \LFXobjeto,
  sobre/.store in          = \LFXsobre,
  domicilio/.store in      = \LFXdomicilio,
  correo/.store in         = \LFXcorreo,
  telefono/.store in       = \LFXtelefono,
  nomenclatura/.store in   = \LFXnomenclatura,
}
\newcommand{\datoslafrox}[1]{\pgfkeys{/lafrox/.cd,#1}}

% Valores por defecto del proyecto.
% IMPORTANTE: todo valor que contenga una coma debe ir entre llaves, o pgfkeys
% lo interpreta como separador de claves.
\datoslafrox{
  empresa       = {LafroX SpA},
  rut           = {77.418.902-K},
  representante = {Alex Aravena},
  cargo         = {Jefe de Proyecto y Apoderado},
  cliente       = {Distribuidora Puelche S.A.},
  licitacion    = {Licitación N.\textdegree{} TFEP-01/2026},
  caso          = {Caso 02 --- Logística},
  documento     = {Propuesta Técnica},
  subtitulo     = {Informe 2},
  alcance       = {Subdocumentos 1--9 y 13},
  formulario    = {Formulario T-22},
  fecha         = {05 de octubre de 2026},
  version       = {1.0},
  logo          = {},
  objeto        = {Proyecto de Plataforma Digital de Misión Crítica},
  sobre         = {Sobre N.\textdegree{} 2 --- Oferta Técnica},
  %  El domicilio se constituye en Valparaíso por exigencia del Art. 39.
  %  PROVISIONAL: confirmar con la identidad definitiva del PROPONENTE.
  domicilio     = {Av. Brasil 2241, Valparaíso},
  correo        = {contacto@lafrox.cl},
  telefono      = {+56 32 250 4100},
}

% Isotipo del kit de marca (carpeta Logo/ del repositorio). Cada proyecto
%  LaTeX lleva su copia en logo/: naranja sobre la banda de la caratula,
%  negro en el encabezado de las hojas interiores.
\newcommand{\LFXisotipoportada}{logo/lafrox_isotipo_naranja.pdf}
\newcommand{\LFXisotipopagina}{logo/lafrox_isotipo_negro.pdf}
% Isotipo del encabezado; si falta el archivo no se dibuja nada.
\newcommand{\LFXisotipoencabezado}{%
  \IfFileExists{\LFXisotipopagina}
    {\raisebox{-0.32\height}{\includegraphics[height=13pt]{\LFXisotipopagina}}%
     \hspace{3pt}}{}}

% Monograma tipografico: marca de respaldo si falta el archivo del isotipo.
%  \lafroxmonograma[lado]   -- por defecto 12mm
%
%  Las coordenadas se escriben como <factor><longitud> (0.5\LFXmonolado) y no
%  como expresion pgfmath (0.5*#1): esta ultima devuelve un numero sin unidad
%  que TikZ interpreta en centimetros, y el monograma se desarma.
\newlength{\LFXmonolado}
\newlength{\LFXmonofont}
\newcommand{\lafroxmonograma}[1][12mm]{%
  \setlength{\LFXmonolado}{#1}%
  \setlength{\LFXmonofont}{0.42\LFXmonolado}%
  \begin{tikzpicture}
    \useasboundingbox (0,0) rectangle (\LFXmonolado,\LFXmonolado);
    \begin{scope}
      \clip[rounded corners=0.09\LFXmonolado]
        (0,0) rectangle (\LFXmonolado,\LFXmonolado);
      \fill[lafroxFuerte] (0,0) rectangle (\LFXmonolado,\LFXmonolado);
      \fill[lafroxBandaC]  (0,0) rectangle (\LFXmonolado,0.15\LFXmonolado);
    \end{scope}
    \node[anchor=center,inner sep=0pt]
      at (0.5\LFXmonolado,0.57\LFXmonolado)
      {\intersemibold\fontsize{\LFXmonofont}{\LFXmonofont}\selectfont
       \color{white}LX};
  \end{tikzpicture}%
}

% Monograma en negativo, para la banda oscura de la portada.
%  Se invierte por completo: chip blanco con las iniciales en el gris de la
%  banda. El monograma normal (relleno negro) desaparece sobre la banda.
\newcommand{\lafroxmonogramaneg}[1][12mm]{%
  \setlength{\LFXmonolado}{#1}%
  \setlength{\LFXmonofont}{0.42\LFXmonolado}%
  \begin{tikzpicture}
    \useasboundingbox (0,0) rectangle (\LFXmonolado,\LFXmonolado);
    \begin{scope}
      \clip[rounded corners=0.09\LFXmonolado]
        (0,0) rectangle (\LFXmonolado,\LFXmonolado);
      \fill[white] (0,0) rectangle (\LFXmonolado,\LFXmonolado);
      \fill[lafroxSobre] (0,0) rectangle (\LFXmonolado,0.15\LFXmonolado);
    \end{scope}
    \node[anchor=center,inner sep=0pt]
      at (0.5\LFXmonolado,0.57\LFXmonolado)
      {\intersemibold\fontsize{\LFXmonofont}{\LFXmonofont}\selectfont
       \color{lafroxBanda}LX};
  \end{tikzpicture}%
}

% Bloque de marca: monograma + razon social
\newcommand{\lafroxmarca}[1][9mm]{%
  \IfFileExists{\LFXisotipopagina}{\raisebox{-0.22\height}{\includegraphics[height=#1]{\LFXisotipopagina}}}{\raisebox{-0.22\height}{\lafroxmonograma[#1]}}\hspace{2.2mm}%
  {\intersemibold\color{lafroxFuerte}\LFXempresa}%
}

% ---------------------------------------------------------------------------
%  7. TITULARES
%
%  Sin filetes, sin cajas y sin oro. La jerarquia se construye con tamano,
%  peso y espacio en blanco, y el numero de capitulo va como rotulo pequeno
%  en mayusculas sobre el titulo.
% ---------------------------------------------------------------------------
\titleformat{\chapter}[display]
  {\normalfont\raggedright}
  {\color{lafroxGris}\LFXrotulo{\chaptertitlename\ \thechapter}}
  {12pt}
  {\intersemibold\fontsize{25pt}{28pt}\selectfont\color{lafroxFuerte}}

\titleformat{\section}
  {\intersemibold\fontsize{15pt}{18pt}\selectfont\color{lafroxTinta}}
  {\textcolor{lafroxFuerte}{\thesection}}{0.6em}{}
\titleformat{\subsection}
  {\intersemibold\fontsize{12pt}{15pt}\selectfont\color{lafroxTinta}}
  {\textcolor{lafroxFuerte}{\thesubsection}}{0.6em}{}
\titleformat{\subsubsection}
  {\intermedium\fontsize{11pt}{14pt}\selectfont\color{lafroxGris}}
  {\thesubsubsection}{0.6em}{}
\titleformat{\paragraph}[runin]
  {\intersemibold\normalsize\color{lafroxTinta}}{}{0pt}{}[.\enspace]

\titlespacing*{\chapter}      {0pt}{-22pt}{30pt}
\titlespacing*{\section}      {0pt}{26pt}{9pt}
\titlespacing*{\subsection}   {0pt}{19pt}{7pt}
\titlespacing*{\subsubsection}{0pt}{15pt}{5pt}
\titlespacing*{\paragraph}    {0pt}{10pt}{0pt}

\setcounter{secnumdepth}{3}
% tocdepth = 3 (no 2): el Art. 40.4 exige "indice detallado con numeracion
% de paginas" y el Art. 5.3 manda la lectura mas exigente ante ambiguedad.
% Debe igualar secnumdepth para que el indice llegue hasta subsubsection.
\setcounter{tocdepth}{3}

% ---------------------------------------------------------------------------
%  8. ENCABEZADO Y PIE  (Art. 40.1 foliacion + Art. 40.2 media firma)
%
%  Un filete tenue y tipografia de 7,5 pt en gris. Nada mas: el encabezado
%  no debe competir con el titular de la pagina.
% ---------------------------------------------------------------------------
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\newcommand{\LFXchico}{\fontsize{7.5pt}{9.5pt}\selectfont\color{lafroxGris}}

% Zona de media firma + folio, extremo inferior derecho.
%  \rowcolors{1}{}{} es obligatorio: la salida de pagina puede ocurrir
%  mientras una tabla con color de fila esta abierta, y sin esto el pie
%  heredaria ese fondo.
%  Los dos bloques del pie llevan [b]: asi comparten la linea base de su
%  ULTIMA fila y el folio queda a la misma altura que la segunda linea del
%  bloque izquierdo. Con la alineacion por omision, cada bloque se apoya en su
%  PRIMERA fila y el de la derecha --- que tiene una fila mas --- cuelga por
%  debajo del otro.
%
%  \arraystretch se reinicia a 1: el 1,42 de las tablas de datos no tiene nada
%  que hacer en un pie de pagina de dos lineas a 7,5 pt.
%
%  \rowcolors{1}{}{} es obligatorio: la salida de pagina puede ocurrir
%  mientras una tabla con color de fila esta abierta, y sin esto el pie
%  heredaria ese fondo.
\newcommand{\LFXpiebase}{%
  \rowcolors{1}{}{}%
  \renewcommand{\arraystretch}{1}%
}

% Rotulo que antecede al numero de pagina.
%  VACIO por omision: el Art. 40.1 exige que la pagina este NUMERADA, no que
%  lleve la palabra "Folio". En un informe preparatorio (Art. 45 - T-22) el
%  numero solo se lee mejor y no compite con el resto del pie.
%
%  Para el Sobre N. 1, que va fisico y con el indice A-5 declarando folio de
%  inicio y de termino por documento, el rotulo si ayuda a que el numero se
%  lea como folio y no como un numero cualquiera. Ahi se recupera con:
%      \renewcommand{\LFXfolio}{Folio}
\newcommand{\LFXfolio}{}

\newcommand{\LFXpiederecho}{%
  \begingroup\LFXpiebase
  {\intermedium\fontsize{9pt}{11pt}\selectfont\color{lafroxTinta}%
    \LFXfoliotexto}%
  \endgroup
}

%  El espacio va DENTRO del condicional: con el rotulo vacio, un
%  "\LFXfolio\ \thepage" dejaria el numero corrido un espacio a la derecha y
%  desalineado respecto del filete de media firma que tiene encima.
\newcommand{\LFXfoliotexto}{%
  \ifx\LFXfolio\@empty\else\LFXfolio\ \fi\thepage}



\newcommand{\LFXpieizquierdo}{%
  \begingroup\LFXpiebase
  \begin{tabular}[b]{@{}l@{}}
    {\LFXchico \LFXempresa}\\
    {\LFXchico \LFXdocumento}
  \end{tabular}%
  \endgroup
}

% ---------------------------------------------------------------------------
%  Cuna del pie: eco de la diagonal de la portada en todas las hojas
%  interiores. Banda negra a sangre con filo naranja, mas alta a la izquierda
%  (misma direccion de pendiente que la portada). Queda por debajo del folio
%  y de la media firma: no debe tocar el pie (Art. 40.1 y 40.2).
%  El pie de cada estilo fija el interruptor en cada pagina: lafrox y plain
%  la encienden; lfxportada y lfxcierre la apagan.
% ---------------------------------------------------------------------------
\newif\ifLFXfranja \LFXfranjatrue
\newcommand{\LFXcunaIzq}{8mm}   % alto de la cuna en el borde izquierdo
\newcommand{\LFXcunaDer}{4mm}   % alto de la cuna en el borde derecho
\newcommand{\LFXcunaFilo}{1.2mm}% grosor del filo naranja
\AddToHook{shipout/background}{%
  \ifLFXfranja
  \put(0,0){\begin{tikzpicture}[remember picture,overlay]
    \fill[lafroxBanda]
      (current page.south west) -- (current page.south east) --
      ([yshift=\LFXcunaDer]current page.south east) --
      ([yshift=\LFXcunaIzq]current page.south west) -- cycle;
    \fill[lafroxNaranja]
      ([yshift=\LFXcunaIzq]current page.south west) --
      ([yshift=\LFXcunaDer]current page.south east) --
      ([yshift=\LFXcunaDer+\LFXcunaFilo]current page.south east) --
      ([yshift=\LFXcunaIzq+\LFXcunaFilo]current page.south west) -- cycle;
  \end{tikzpicture}}%
  \fi}

\fancypagestyle{lafrox}{%
  \fancyhf{}
  \fancyhead[L]{\LFXisotipoencabezado{\LFXchico\LFXempresa}}
  \fancyhead[R]{{\LFXchico\nouppercase{\leftmark}}}
  \fancyfoot[L]{\global\LFXfranjatrue\LFXpieizquierdo}
  \fancyfoot[R]{\LFXpiederecho}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{%
    \vspace{3pt}%
    \hbox to\headwidth{\color{lafroxTenue}\leaders\hrule height 0.5pt\hfill}}
}

% Las aperturas de capitulo heredan foliacion y firma: sin excepciones (Art. 40.1).
%  \headrule se anula explicitamente: no basta con headrulewidth=0, porque el
%  \headrule del estilo lafrox dibuja el filete por su cuenta y la pagina de
%  apertura quedaria con una linea suelta sobre el titulo.
\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyfoot[L]{\global\LFXfranjatrue\LFXpieizquierdo}
  \fancyfoot[R]{\LFXpiederecho}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{}
}

% Pie solo con folio, en el color que se le indique.
%  El color queda como parametro por si una pieza futura necesita el pie en
%  negativo. Desde la v2.2 ni la portada ni la contraportada lo usan: ambas
%  tintan solo la cabecera y dejan el pie sobre papel blanco, que es la unica
%  forma de que el folio sobreviva a una fotocopia (Art. 40.1, excluyente).
\newcommand{\LFXpiefolioen}[1]{%
  \begingroup\LFXpiebase
  {\intermedium\fontsize{9pt}{11pt}\selectfont\color{#1}%
    \LFXfoliotexto}%
  \endgroup
}

% Portada: sin encabezado, pero CON folio (no se admiten paginas sin numerar).
%  Aqui va el folio solo, sin la zona de media firma: el Art. 40.2 pide media
%  firma en cada pagina y firma COMPLETA en la caratula, y esa la aporta el
%  bloque de firma de la propia portada.
%  Folio en TINTA: desde la v2.2 la banda ocupa solo la cabecera y el pie
%  queda sobre papel blanco. Antes iba en blanco sobre la cuna, y su
%  legibilidad dependia de que la diagonal exterior alcanzara el margen
%  derecho -- un folio ilegible es causal de exclusion (Art. 40.1), asi que
%  no debe depender de la geometria del arte.
\fancypagestyle{lfxportada}{%
  \fancyhf{}
  \fancyfoot[R]{\global\LFXfranjafalse\LFXpiefolioen{lafroxTinta}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{}
}

% Contraportada: mismo pie desnudo, pero en tinta -- ahi el fondo es claro.
\fancypagestyle{lfxcierre}{%
  \fancyhf{}
  \fancyfoot[R]{\global\LFXfranjafalse\LFXpiefolioen{lafroxTinta}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{}
}

\pagestyle{lafrox}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\pagenumbering{arabic}

% Marca de agua de borrador, al fondo y muy tenue.
%  Se salta el folio 1. Mientras la portada fue una cuna oscura a sangre la
%  marca era invisible ahi; desde la v2.2 la caratula es clara y la diagonal
%  cruzaba justo el bloque de identificacion del Art. 49.1, que es el que
%  tiene que leerse sin estorbo. El estado ya se declara dos veces en la
%  propia caratula (rotulo de la banda y campo "Estado"), asi que no se
%  pierde el aviso de borrador.
\ifLFX@borrador
  \AddToShipoutPictureBG{%
    \ifnum\value{page}>1
      \put(\LenToUnit{0.5\paperwidth},\LenToUnit{0.42\paperheight}){%
        \makebox(0,0){\rotatebox{54}{%
          \intersemibold\fontsize{74pt}{74pt}\selectfont
          \color{lafroxFuerte!10}BORRADOR}}}%
    \fi}
\fi

% ---------------------------------------------------------------------------
%  9. TABLAS
%
%  Sin relleno de cabecera, sin filas cebra y sin lineas verticales: tres
%  filetes horizontales y espacio. Es donde mas se nota el cambio de tema, y
%  es tambien la forma que mejor aguanta un catalogo de cien filas.
% ---------------------------------------------------------------------------

% Columnas de ancho absoluto
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\RaggedLeft\arraybackslash}p{#1}}
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

% Columnas de ancho fraccionario del bloque de texto: F{0.25} G{0.20} ...
% Utiles para fijar una columna angosta sin recurrir a centimetros.
% No sirven para cuadrar la tabla entera: de eso se encarga la columna Y.
\newcommand{\LFXcolw}[1]{\dimexpr #1\textwidth-2\tabcolsep\relax}
\newcolumntype{F}[1]{>{\RaggedRight\arraybackslash}p{\LFXcolw{#1}}}
\newcolumntype{G}[1]{>{\Centering\arraybackslash}p{\LFXcolw{#1}}}
\newcolumntype{H}[1]{>{\RaggedLeft\arraybackslash}p{\LFXcolw{#1}}}

\renewcommand{\arraystretch}{1.42}
\setlength{\arrayrulewidth}{0.5pt}
\arrayrulecolor{lafroxLinea}
\setlength{\heavyrulewidth}{0.6pt}
\setlength{\lightrulewidth}{0.4pt}
\setlength{\aboverulesep}{4pt}
\setlength{\belowrulesep}{6pt}

\captionsetup{
  font={footnotesize,color=lafroxGris},
  labelfont={color=lafroxFuerte},
  labelsep=quad, skip=7pt,
  justification=raggedright, singlelinecheck=false}
\captionsetup[table]{position=top,skip=6pt}

% Celda de cabecera: peso, no color de fondo.
\newcommand{\cab}[1]{{\intersemibold\color{lafroxTinta}#1}}

% ---------------------------------------------------------------------------
%  tablalafrox -- tabla institucional unica de la clase.
%
%  Esta construida sobre xltabular: rompe de pagina sola, repite la cabecera,
%  rotula la continuacion y --- lo importante --- calcula el ancho de las
%  columnas elasticas para que la tabla mida exactamente \textwidth. Por eso
%  la especificacion de columnas DEBE incluir al menos una columna Y.
%
%  El cuerpo se captura como argumento (+b). Es obligatorio: tabularx y sus
%  derivados leen su contenido de una sola vez y no sobreviven a un
%  \newenvironment partido entre codigo de apertura y de cierre.
%
%  #1 caption   #2 label   #3 columnas (al menos una Y)   #4 fila de cabecera
%
%  \begin{tablalafrox}{Reparto de alcance}{tab:etapas}{L{2.2cm} Y G{0.22}}
%    {\cab{Etapa} & \cab{Alcance} & \cab{Produccion}}
%    Etapa 1 & ... & ... \\
%  \end{tablalafrox}
% ---------------------------------------------------------------------------
\NewDocumentEnvironment{tablalafrox}{m m m m +b}{%
  \par
  \LFXfiletear{#5}%
  \LFXcuerpotabla
  \setlength{\LTpre}{12pt}\setlength{\LTpost}{16pt}%
  % El cuerpo con filetes se entrega como tokens reales, no dentro de una
  % macro: longtable necesita ver las filas en la entrada para cortar pagina.
  \LFXconcuerpo{%
  \begin{xltabular}{\textwidth}{#3}
    \caption{#1}\label{#2}\\[2pt]
    \LFXtopruleoriginal #4 \\ \midrule
    \endfirsthead
    % Los rotulos van en una caja de ancho cero: si midieran su texto real,
    % longtable ensancharia la primera columna de TODA la tabla para caberlos.
    \multicolumn{1}{@{}l@{}}{\makebox[0pt][l]{%
      \fontsize{9pt}{10.5pt}\selectfont\color{lafroxGris}%
      Tabla \thetable\ --- continuación}}\\[3pt]
    \LFXtopruleoriginal #4 \\ \midrule
    \endhead
    \midrule
    \multicolumn{1}{@{}l@{}}{\makebox[0pt][l]{%
      \fontsize{9pt}{10.5pt}\selectfont\color{lafroxGris}%
      continúa en la página siguiente}}\\
    \endfoot
    \bottomrule
    \endlastfoot}%
}{}

% Alias retrocompatible
\NewDocumentEnvironment{tablalarga}{m m m m +b}
  {\begin{tablalafrox}{#1}{#2}{#3}{#4}#5\end{tablalafrox}}{}

% Referencia a planilla externa -- convencion NN_subdocumento/entrega_N/tablas/
%   \tablaref{7}{Volumetria de despacho}{04_arquitectura/entrega_2/tablas/Dim.xlsx!Despacho}
%  Sin relleno ni marco: un filete tenue arriba y el dato. Varias referencias
%  seguidas forman una lista con una sola linea entre cada par, no dos.
\newcommand{\tablaref}[3]{%
  \par\addvspace{11pt}%
  \noindent{\color{lafroxLinea}\rule{\textwidth}{0.4pt}}\par
  \vspace{5pt}%
  \noindent{\intersemibold\color{lafroxFuerte}Tabla #1}%
  \quad{\color{lafroxTinta}#2}\par
  \vspace{2pt}%
  \noindent{\fontsize{9pt}{11pt}\selectfont\color{lafroxGris}%
    Planilla\quad\texttt{#3}}%
  \par\addvspace{11pt}%
}

% ---------------------------------------------------------------------------
% 10. CITAS Y NOTAS DE TRABAJO
%
%  Los unicos dos recursos de este tipo. No hay cajas de color, etiquetas de
%  trazabilidad, fichas de indicadores ni marcador \pendiente: la marca de lo
%  que falta se escribe dentro de una \nota, que se apaga entera con [final].
% ---------------------------------------------------------------------------

% \begin{cita}{Caso 02 --- Logistica, Cap. 15}  ...  \end{cita}
\newenvironment{cita}[1]
  {\def\LFXcitafuente{#1}%
   \par\addvspace{11pt}%
   \begingroup
   \setlength{\leftskip}{1.4em}%
   \setlength{\rightskip}{1.4em}%
   \small\color{lafroxGris}
   \noindent\llap{\textcolor{lafroxLinea}{\vrule width 1.5pt height 0.9em depth 0.3em}\hspace{1.2em}}%
  }
  {\par\normalsize
   \hfill{\fontsize{9pt}{10.5pt}\selectfont\color{lafroxGris}%
          \textemdash\ \LFXcitafuente}%
   \par\endgroup\addvspace{11pt}%
  }

% Notas de orientacion y pendientes: se apagan de golpe con [final] o
% [sinnotas]. Un solo interruptor para todo el andamiaje de redaccion.
\newcommand{\nota}[1]{%
  \ifLFX@notas
    \par\addvspace{7pt}%
    \begingroup
    \setlength{\leftskip}{1.1em}%
    \noindent\llap{\textcolor{lafroxFuerte!40}{%
      \vrule width 1.5pt height 0.82em depth 0.25em}\hspace{0.9em}}%
    {\fontsize{9pt}{11.5pt}\selectfont\color{lafroxGris}#1}%
    \par\endgroup\addvspace{9pt}%
  \fi}

% Marcador visible para figuras que aun no se han incorporado al PDF.
% Se deja siempre presente en la posicion exacta donde falta la ilustracion.
\newcommand{\LFXfiguraPendiente}{%
  \par\addvspace{6pt}%
  \begin{center}
    \fbox{%
      \parbox[c][2.8cm][c]{0.90\linewidth}{%
        \centering
        {\intersemibold\fontsize{12pt}{14pt}\selectfont\color{lafroxFuerte}FIGURA PENDIENTE}\par
        \vspace{4pt}
        {\fontsize{9pt}{11pt}\selectfont\color{lafroxGris}por insertar en esta posición}%
      }%
    }%
  \end{center}
  \par\addvspace{6pt}%
}

% ---------------------------------------------------------------------------
% 11. FIGURAS Y ANEXOS HORIZONTALES
% ---------------------------------------------------------------------------
%  \figuralafrox{ancho relativo}{archivo}{caption}{label}
\newcommand{\figuralafrox}[4]{%
  \begin{figure}[htbp]\centering
    \includegraphics[width=#1\textwidth]{#2}
    \caption{#3}\label{#4}
  \end{figure}}

\newenvironment{anexohorizontal}{\begin{landscape}}{\end{landscape}}

% ---------------------------------------------------------------------------
% 11 bis. SUBDOCUMENTOS EN CARPETA PROPIA
%
%  Cada subdocumento del T-7 vive en su carpeta, autocontenido, y main.tex lo
%  llama por el nombre de la carpeta. Mover la carpeta y cambiar la ruta en la
%  llamada es TODO lo que hace falta para reubicarlo: nada dentro del capitulo
%  conoce donde esta montado.
%
%      NN_nombre/
%        contenido.tex     <- el \chapter y el texto
%        figuras/          <- imagenes del capitulo
%        tablas/           <- fragmentos .tex, si el capitulo se parte
%
%  En main.tex:              \subdocumento{07_plan_trabajo_edt}
%  Dentro de contenido.tex:  \parte{tablas/catalogo_rf}
%                            \figuralafrox{0.9}{figuras/edt.png}{...}{...}
%
%  Se usa \import y no \input: con \input, un \input anidado dentro del
%  capitulo se resuelve desde la carpeta de main.tex y no desde la del
%  capitulo, de modo que mover la carpeta rompe las rutas internas --- que es
%  exactamente lo que esta estructura existe para evitar.
\RequirePackage{import}

%  \graphicspath se fija DENTRO del grupo, asi que vale solo mientras dura la
%  importacion y dos capitulos pueden tener cada uno su figuras/x.png sin
%  pisarse. Las figuras se componen al construir la caja, dentro del grupo,
%  aunque el flotante se despache paginas despues.
\newcommand{\subdocumento}[1]{%
  \begingroup
  \graphicspath{{#1/}{#1/figuras/}{#1/diagramas/}}%
  \import{#1/}{contenido.tex}%
  \endgroup}

%  Fragmento interno de un subdocumento, relativo a SU carpeta. Sin extension.
\newcommand{\parte}[1]{\subimport{}{#1.tex}}

% ---------------------------------------------------------------------------
% 12. PAGINAS PRELIMINARES
% ---------------------------------------------------------------------------
%  Indice sin guias de puntos: la alineacion del numero de folio a la derecha
%  basta, y los puntos son ruido.
\titlecontents{chapter}[0pt]
  {\addvspace{13pt}\intersemibold\color{lafroxTinta}}
  {\textcolor{lafroxFuerte}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{section}[1.5em]
  {\addvspace{3pt}\color{lafroxTinta}}
  {\textcolor{lafroxGris}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{subsection}[3.4em]
  {\fontsize{9.5pt}{12pt}\selectfont\color{lafroxGris}}
  {\thecontentslabel\enspace}{}
  {\hfill\contentspage}
% Cuarto nivel: mismo lenguaje que subsection, un punto mas chico y mas
% sangria. Necesario porque tocdepth=3 lo activa (ver seccion 7) y sin este
% \titlecontents, book/report caeria en \l@subsubsection con guias de puntos
% -- justo lo que este indice evita en los demas niveles.
\titlecontents{subsubsection}[5.2em]
  {\fontsize{9pt}{11.5pt}\selectfont\color{lafroxGris}}
  {\thecontentslabel\enspace}{}
  {\hfill\contentspage}

% Entradas de las listas de tablas y de figuras. Mismo lenguaje que el indice
% general: sin guias de puntos y con el folio alineado a la derecha.
\titlecontents{table}[0pt]
  {\addvspace{3pt}\color{lafroxTinta}}
  {\textcolor{lafroxGris}{Tabla \thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{figure}[0pt]
  {\addvspace{3pt}\color{lafroxTinta}}
  {\textcolor{lafroxGris}{Figura \thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}

% Titulo de pagina preliminar, mismo lenguaje que el de capitulo
\newcommand{\LFXtitulopreliminar}[1]{%
  \noindent
  {\intersemibold\fontsize{25pt}{28pt}\selectfont\color{lafroxFuerte}#1}%
  \par\vspace{22pt}}

% Indice general (Art. 40.4: indice detallado con folios)
\newcommand{\indicelafrox}{%
  \phantomsection\addcontentsline{toc}{chapter}{Índice general}%
  \LFXtitulopreliminar{Índice general}%
  \@starttoc{toc}%
  \clearpage}

% Indice de tablas y de figuras. Se generan solos a partir de los \caption:
% no hay ninguna lista que mantener a mano.
\newcommand{\listatablaslafrox}{%
  \phantomsection\addcontentsline{toc}{chapter}{Lista de tablas}%
  \LFXtitulopreliminar{Lista de tablas}%
  \@starttoc{lot}%
  \clearpage}

\newcommand{\listafiguraslafrox}{%
  \phantomsection\addcontentsline{toc}{chapter}{Lista de figuras}%
  \LFXtitulopreliminar{Lista de figuras}%
  \@starttoc{lof}%
  \clearpage}

% Los tres indices, en el orden en que los espera un evaluador
\newcommand{\preliminareslafrox}{%
  \indicelafrox
  \listatablaslafrox
  \listafiguraslafrox}

% Subtitulo de pagina de control: sin filete, solo peso y aire
\newcommand{\LFXsubtitulocontrol}[1]{%
  \par\addvspace{6pt}\noindent
  {\intersemibold\fontsize{15pt}{18pt}\selectfont\color{lafroxTinta}#1}%
  \par\vspace{10pt}}

% Hoja de control de versiones
%  \begin{controlversiones} \versionfila{1.0}{05-10-2026}{Autor}{Cambio} \end{...}
\NewDocumentEnvironment{controlversiones}{+b}{%
  \LFXsubtitulocontrol{Control de versiones}%
  \LFXcuerpotabla
  \setlength{\LTpre}{2pt}\setlength{\LTpost}{16pt}%
  \begin{xltabular}{\textwidth}{C{1.7cm} C{2.3cm} L{3.6cm} Y}
    \LFXtopruleoriginal
    \cab{Versión} & \cab{Fecha} & \cab{Responsable} & \cab{Cambio} \\
    \midrule
    \endfirsthead
    \LFXtopruleoriginal
    \cab{Versión} & \cab{Fecha} & \cab{Responsable} & \cab{Cambio} \\
    \midrule
    \endhead
    \endfoot
    \bottomrule
    \endlastfoot
    #1
  \end{xltabular}%
}{}
\newcommand{\versionfila}[4]{#1 & #2 & #3 & #4 \\}

% Hoja resumen con folio inicial por seccion (Art. 40.3)
%  \begin{hojaresumen} \resumenfila{Arquitectura logica}{cap:arqlog} \end{...}
\newcounter{LFXresumen}
\NewDocumentEnvironment{hojaresumen}{+b}{%
  \LFXsubtitulocontrol{Hoja resumen del sobre}%
  \nota{Exigida por el Art. 40.3 de las Bases Administrativas: el folio inicial de
        cada sección debe corresponder exactamente a la foliación del documento.
        Los folios se resuelven solos vía \texttt{\textbackslash pageref}.}%
  \LFXcuerpotabla
  \setlength{\LTpre}{6pt}\setlength{\LTpost}{16pt}%
  \begin{xltabular}{\textwidth}{C{1.5cm} Y C{2.8cm}}
    \LFXtopruleoriginal
    \cab{N.\textdegree} & \cab{Sección} & \cab{Folio inicial} \\
    \midrule
    \endfirsthead
    \LFXtopruleoriginal
    \cab{N.\textdegree} & \cab{Sección} & \cab{Folio inicial} \\
    \midrule
    \endhead
    \endfoot
    \bottomrule
    \endlastfoot
    #1
  \end{xltabular}%
}{}
\newcommand{\resumenfila}[2]{%
  \stepcounter{LFXresumen}\theLFXresumen & #1 & \pageref{#2} \\}

% ---------------------------------------------------------------------------
% 13. REFERENCIAS APA 7. ed. (Art. 40.4) -- opcion de clase [apa]
% ---------------------------------------------------------------------------
\ifLFX@apa
  \RequirePackage[style=apa,backend=biber]{biblatex}
  \DeclareLanguageMapping{spanish}{spanish-apa}
\fi

% ---------------------------------------------------------------------------
% 14. HYPERREF (siempre al final del preambulo de clase)
% ---------------------------------------------------------------------------
\RequirePackage[hidelinks,bookmarksnumbered]{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=lafroxFuerte, urlcolor=lafroxFuerte, citecolor=lafroxFuerte,
  pdftitle={\LFXdocumento\ --- \LFXsubtitulo},
  pdfauthor={\LFXempresa},
  pdfsubject={\LFXlicitacion\ --- \LFXcaso},
  pdfkeywords={licitacion, oferta tecnica, logistica, Puelche},
  pdfcreator={LuaLaTeX + lafrox.cls}}
\RequirePackage{bookmark}

% ---------------------------------------------------------------------------
% 15. PORTADA
%
%  Es la unica pieza expresiva de la plantilla y queda fuera del tema
%  minimalista a proposito.
% ---------------------------------------------------------------------------
\InputIfFileExists{lafrox-portada.tex}{}{%
  \ClassWarning{lafrox}{No se encontro lafrox-portada.tex:
    la macro \string\portadalafrox\space no estara disponible}}

\endinput
