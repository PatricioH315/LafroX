%% ============================================================================
%%  lafrox.cls -- Clase corporativa LafroX
%%  Propuestas tecnicas para la Licitacion N. TFEP-01/2026
%%  Caso 02 - Logistica (Distribuidora Puelche S.A.)
%%
%%  Motor: LuaLaTeX (obligatorio -- usa fontspec)
%%  Compilar: latexmk demo.tex     (el latexmkrc ya fija lualatex)
%%
%%  Tema: minimalista. Tipografia Inter en todo el documento, sin filetes
%%  decorativos, sin rellenos de color en las tablas y sin filas cebra. El
%%  unico elemento expresivo es la portada, que conserva su banda diagonal.
%%
%%  Cumplimiento formal cableado en la clase (Bases Administrativas, Art. 40):
%%    40.1  Foliacion correlativa, sin saltos, extremo inferior derecho
%%    40.2  Zona de media firma en el extremo inferior derecho de cada pagina
%%    40.3  Hoja resumen con folio inicial por seccion
%%    40.4  Carta u oficio vertical; cuerpo >= 11 pt; tablas y figuras >= 9 pt
%% ============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lafrox}[2026/09/17 v2.1 Clase corporativa LafroX, tema minimalista]

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
%  Casi monocroma. El violeta es el unico acento del cuerpo del documento;
%  el oro queda reservado a la portada y no aparece en ninguna pagina de
%  contenido. No hay colores semanticos de severidad ni de estado.
% ---------------------------------------------------------------------------
\RequirePackage[table,dvipsnames]{xcolor}

\definecolor{lafroxVioleta}{HTML}{2B1A4D}  % acento
\definecolor{lafroxAzul}   {HTML}{1B3050}  % secundario (portada)
\definecolor{lafroxAcento} {HTML}{B8901F}  % oro: SOLO portada
\definecolor{lafroxTinta}  {HTML}{17171E}  % cuerpo de texto
\definecolor{lafroxGris}   {HTML}{5B646E}  % texto secundario
\definecolor{lafroxLinea}  {HTML}{C9C6D1}  % filetes de tabla
\definecolor{lafroxTenue}  {HTML}{D8D5DF}  % filetes de encabezado y pie
\definecolor{lafroxBg}     {HTML}{F5F4F8}  % fondo de portada

% ---------------------------------------------------------------------------
%  4. TIPOGRAFIA
%
%  Inter en todo el documento, sin serif. Inter es el sustituto abierto (SIL
%  OFL) de la familia SF de Apple: mismo esqueleto geometrico-humanista y
%  altura de x alta. Las SF de Apple no son redistribuibles para composicion
%  de documentos, asi que no se usan.
%
%  El cuerpo queda en 11 pt, que es el minimo del Art. 40.4. No bajarlo.
% ---------------------------------------------------------------------------
\RequirePackage[sfdefault]{inter}
%  IBM Plex Mono para \texttt: rutas de planilla, opciones de clase y codigos.
%  Comparte el esqueleto humanista-geometrico de Inter, asi que no desentona
%  como si desentonaba el mono de Latin Modern que trae LaTeX por defecto.
\RequirePackage[scale=0.92]{plex-mono}
\RequirePackage{microtype}

% Por si el paquete se carga en modo type1, donde no define los pesos OTF
\providecommand{\interthin}{\normalfont}
\providecommand{\interlight}{\normalfont}
\providecommand{\intermedium}{\bfseries}
\providecommand{\intersemibold}{\bfseries}

\RequirePackage[spanish,es-tabla,es-noquoting,es-nolists]{babel}
\RequirePackage{csquotes}

\linespread{1.18}
\setlength{\parskip}{7pt}
\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{2em}

% Cuerpos minimos exigidos por las Bases. No bajar de aqui.
%  En tabla se fuerzan cifras de ancho fijo: las columnas de codigos y de
%  cantidades tienen que alinearse verticalmente.
\newcommand{\LFXcuerpotabla}{%
  \fontsize{9.5pt}{12.5pt}\selectfont
  \addfontfeature{Numbers=Monospaced}}
\newcommand{\LFXcuerpofigura}{\fontsize{9pt}{11.5pt}\selectfont}

% Rotulo pequeno en mayusculas con interletraje abierto. Es el unico recurso
% "grafico" que se permite en los titulares del tema minimalista.
\newcommand{\LFXrotulo}[1]{%
  {\fontsize{7.5pt}{9pt}\selectfont
   \addfontfeature{LetterSpace=14}\intermedium
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
\RequirePackage{ragged2e}

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
  asignatura/.store in     = \LFXasignatura,
  unidad/.store in         = \LFXunidad,
  profesor/.store in       = \LFXprofesor,
  logo/.store in           = \LFXlogo,
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
  asignatura    = {Taller de Formulación de Proyectos Informáticos (ICI-5444)},
  unidad        = {Escuela de Informática, PUCV},
  profesor      = {Antonio Moya Villegas},
  logo          = {},
}

% Monograma tipografico: marca provisional mientras no exista archivo de logo.
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
      \fill[lafroxVioleta] (0,0) rectangle (\LFXmonolado,\LFXmonolado);
      \fill[lafroxAcento]  (0,0) rectangle (\LFXmonolado,0.15\LFXmonolado);
    \end{scope}
    \node[anchor=center,inner sep=0pt]
      at (0.5\LFXmonolado,0.57\LFXmonolado)
      {\intersemibold\fontsize{\LFXmonofont}{\LFXmonofont}\selectfont
       \color{white}LX};
  \end{tikzpicture}%
}

% Bloque de marca: monograma + razon social
\newcommand{\lafroxmarca}[1][9mm]{%
  \raisebox{-0.22\height}{\lafroxmonograma[#1]}\hspace{2.2mm}%
  {\intersemibold\color{lafroxVioleta}\LFXempresa}%
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
  {\intersemibold\fontsize{25pt}{28pt}\selectfont\color{lafroxVioleta}}

\titleformat{\section}
  {\intersemibold\fontsize{15pt}{18pt}\selectfont\color{lafroxTinta}}
  {\textcolor{lafroxVioleta}{\thesection}}{0.6em}{}
\titleformat{\subsection}
  {\intersemibold\fontsize{12pt}{15pt}\selectfont\color{lafroxTinta}}
  {\textcolor{lafroxVioleta}{\thesubsection}}{0.6em}{}
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
\setcounter{tocdepth}{2}

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

\newcommand{\LFXfolio}{Folio}

\newcommand{\LFXpiederecho}{%
  \begingroup\LFXpiebase
  \begin{tabular}[b]{@{}r@{}}
    \ifLFX@firma
      \textcolor{lafroxTenue}{\rule{3.4cm}{0.5pt}}\\[1pt]
      {\fontsize{6.5pt}{8pt}\selectfont\color{lafroxGris}%
        Media firma --- \LFXrepresentante}\\[5pt]
    \fi
    {\intermedium\fontsize{9pt}{11pt}\selectfont\color{lafroxTinta}%
      \LFXfolio\ \thepage}
  \end{tabular}%
  \endgroup
}

\newcommand{\LFXpieizquierdo}{%
  \begingroup\LFXpiebase
  \begin{tabular}[b]{@{}l@{}}
    {\LFXchico \LFXempresa\ \textperiodcentered\ \LFXlicitacion}\\
    {\LFXchico \LFXdocumento\ \textperiodcentered\ \LFXsubtitulo\
      \textperiodcentered\ v\LFXversion}
  \end{tabular}%
  \endgroup
}

\fancypagestyle{lafrox}{%
  \fancyhf{}
  \fancyhead[L]{{\LFXchico\LFXempresa}}
  \fancyhead[R]{{\LFXchico\nouppercase{\leftmark}}}
  \fancyfoot[L]{\LFXpieizquierdo}
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
  \fancyfoot[L]{\LFXpieizquierdo}
  \fancyfoot[R]{\LFXpiederecho}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{}
}

% Pie solo con folio, para la portada
\newcommand{\LFXpiefolio}{%
  \begingroup\LFXpiebase
  {\intermedium\fontsize{9pt}{11pt}\selectfont\color{lafroxTinta}%
    \LFXfolio\ \thepage}%
  \endgroup
}

% Portada: sin encabezado, pero CON folio (no se admiten paginas sin numerar).
%  Aqui va el folio solo, sin la zona de media firma: el Art. 40.2 pide media
%  firma en cada pagina y firma COMPLETA en la caratula, y esa la aporta la
%  linea "Firma del representante" de la propia portada. Repetir la media
%  firma, ademas, chocaba con el bloque academico del pie de la portada.
\fancypagestyle{lfxportada}{%
  \fancyhf{}
  \fancyfoot[R]{\LFXpiefolio}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\headrule}{}
}

\pagestyle{lafrox}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\pagenumbering{arabic}

% Marca de agua de borrador, al fondo y muy tenue
\ifLFX@borrador
  \AddToShipoutPictureBG{%
    \put(\LenToUnit{0.5\paperwidth},\LenToUnit{0.42\paperheight}){%
      \makebox(0,0){\rotatebox{54}{%
        \intersemibold\fontsize{74pt}{74pt}\selectfont
        \color{lafroxVioleta!10}BORRADOR}}}}
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
  labelfont={color=lafroxVioleta},
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
  \LFXcuerpotabla
  \setlength{\LTpre}{12pt}\setlength{\LTpost}{16pt}%
  \begin{xltabular}{\textwidth}{#3}
    \caption{#1}\label{#2}\\[2pt]
    \toprule #4 \\ \midrule
    \endfirsthead
    % Los rotulos van en una caja de ancho cero: si midieran su texto real,
    % longtable ensancharia la primera columna de TODA la tabla para caberlos.
    \multicolumn{1}{@{}l@{}}{\makebox[0pt][l]{%
      \fontsize{8pt}{9pt}\selectfont\color{lafroxGris}%
      Tabla \thetable\ --- continuación}}\\[3pt]
    \toprule #4 \\ \midrule
    \endhead
    \midrule
    \multicolumn{1}{@{}l@{}}{\makebox[0pt][l]{%
      \fontsize{8pt}{9pt}\selectfont\color{lafroxGris}%
      continúa en la página siguiente}}\\
    \endfoot
    \bottomrule
    \endlastfoot
    #5
  \end{xltabular}%
}{}

% Alias retrocompatible
\NewDocumentEnvironment{tablalarga}{m m m m +b}
  {\begin{tablalafrox}{#1}{#2}{#3}{#4}#5\end{tablalafrox}}{}

% Referencia a planilla externa -- convencion de Entrega 2/
%   \tablaref{7}{Volumetria de despacho}{05_arquitectura_fisica/tablas/Dim.xlsx!Despacho}
%  Sin relleno ni marco: un filete tenue arriba y el dato. Varias referencias
%  seguidas forman una lista con una sola linea entre cada par, no dos.
\newcommand{\tablaref}[3]{%
  \par\addvspace{11pt}%
  \noindent{\color{lafroxLinea}\rule{\textwidth}{0.4pt}}\par
  \vspace{5pt}%
  \noindent{\intersemibold\color{lafroxVioleta}Tabla #1}%
  \quad{\color{lafroxTinta}#2}\par
  \vspace{2pt}%
  \noindent{\fontsize{8.5pt}{10.5pt}\selectfont\color{lafroxGris}%
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
   \hfill{\fontsize{8.5pt}{10pt}\selectfont\color{lafroxGris}%
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
    \noindent\llap{\textcolor{lafroxVioleta!40}{%
      \vrule width 1.5pt height 0.82em depth 0.25em}\hspace{0.9em}}%
    {\fontsize{8.5pt}{11pt}\selectfont\color{lafroxGris}#1}%
    \par\endgroup\addvspace{9pt}%
  \fi}

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
% 12. PAGINAS PRELIMINARES
% ---------------------------------------------------------------------------
%  Indice sin guias de puntos: la alineacion del numero de folio a la derecha
%  basta, y los puntos son ruido.
\titlecontents{chapter}[0pt]
  {\addvspace{13pt}\intersemibold\color{lafroxTinta}}
  {\textcolor{lafroxVioleta}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{section}[1.5em]
  {\addvspace{3pt}\color{lafroxTinta}}
  {\textcolor{lafroxGris}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{subsection}[3.4em]
  {\fontsize{9.5pt}{12pt}\selectfont\color{lafroxGris}}
  {\thecontentslabel\enspace}{}
  {\hfill\contentspage}

% Titulo de pagina preliminar, mismo lenguaje que el de capitulo
\newcommand{\LFXtitulopreliminar}[1]{%
  {\intersemibold\fontsize{25pt}{28pt}\selectfont\color{lafroxVioleta}#1}%
  \par\vspace{22pt}}

% Indice general (Art. 40.4: indice detallado con folios)
\newcommand{\indicelafrox}{%
  \phantomsection\addcontentsline{toc}{chapter}{Índice general}%
  \LFXtitulopreliminar{Índice general}%
  \@starttoc{toc}%
  \clearpage}

% Subtitulo de pagina de control: sin filete, solo peso y aire
\newcommand{\LFXsubtitulocontrol}[1]{%
  \par\addvspace{6pt}%
  {\intersemibold\fontsize{15pt}{18pt}\selectfont\color{lafroxTinta}#1}%
  \par\vspace{10pt}}

% Hoja de control de versiones
%  \begin{controlversiones} \versionfila{1.0}{05-10-2026}{Autor}{Cambio} \end{...}
\NewDocumentEnvironment{controlversiones}{+b}{%
  \LFXsubtitulocontrol{Control de versiones}%
  \LFXcuerpotabla
  \setlength{\LTpre}{2pt}\setlength{\LTpost}{16pt}%
  \begin{xltabular}{\textwidth}{C{1.7cm} C{2.3cm} L{3.6cm} Y}
    \toprule
    \cab{Versión} & \cab{Fecha} & \cab{Responsable} & \cab{Cambio} \\
    \midrule
    \endfirsthead
    \toprule
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
    \toprule
    \cab{N.\textdegree} & \cab{Sección} & \cab{Folio inicial} \\
    \midrule
    \endfirsthead
    \toprule
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
  linkcolor=lafroxVioleta, urlcolor=lafroxVioleta, citecolor=lafroxVioleta,
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
