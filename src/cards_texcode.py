BLACKANDWHITENUMBERS = """
\\documentclass{standalone}
\\usepackage{tikz}
\\usepackage{xcolor}
\\usepackage{amsmath}
\\usepackage{varwidth}
\\usepackage{pgfornament}
\\usetikzlibrary{fit,shapes,positioning,backgrounds}
\\newcommand{\\magnitude}[1] {
    \\ifnum #1 = 0
        ~
    \\else
        \\times 10^{#1}~
    \\fi
}
\\tikzset{
    namenode/.style={
        execute at begin node={\\begin{varwidth}{3cm}\\begin{center}\\footnotesize},
        execute at end node={\\end{center}\\end{varwidth}},
    },
    formulaenode/.style={
        execute at begin node={\\footnotesize $\\textcolor{gray}},
        execute at end node={$},
    },
    valuenode/.style={
        execute at begin node={\\footnotesize $},
        execute at end node={$},
    },
    symbolnode/.style={
        scale=2,
        execute at begin node={\\Huge $},
        execute at end node={$},
    },
    diagsymbolnode/.style={
        execute at begin node={\\Large $},
        execute at end node={$},
    },
}
\\begin{document}
\\begin{tikzpicture}[x=1cm,y=1cm]
    \\def\\w{5};
    \\def\\h{7};
    \\def\\k{0.5};

    \\coordinate (north) at (0,0.5*\\h);
    \\coordinate (south) at (0,-0.5*\\h);
    \\coordinate (east) at (0.5*\\w,0);
    \\coordinate (west) at (-0.5*\\w,0);

    \\def\\name{%s};
    \\def\\symbol{%s};
    \\def\\formulae{%s};
    \\def\\value{%s};
    \\def\\power{%s};
    \\def\\unit{%s};
    \\def\\order{%s};

    \\draw[thick,rounded corners=2pt] (-0.5*\\w,-0.5*\\h) rectangle (0.5*\\w,0.5*\\h);
    \\draw[thin,rounded corners=2pt] (-0.5*\\w+0.1,-0.5*\\h+0.1) rectangle (0.5*\\w-0.1,0.5*\\h-0.1);

    \\path (-0.35*\\w,-0.35*\\h) to [ornament=88] (-0.35*\\w,0.35*\\h);
    \\path (0.35*\\w,-0.35*\\h) to [ornament=88] (0.35*\\w,0.35*\\h);

    \\node[symbolnode] (C) at (0,0) {\\symbol};
    \\node[diagsymbolnode] (D1) at (0.5*\\w-\\k,-0.5*\\h+\\k) {\\order};
    \\node[diagsymbolnode] (D2) at (0.5*\\w-\\k,0.5*\\h-\\k) {\\order};
    \\node[diagsymbolnode] (D3) at (-0.5*\\w+\\k,-0.5*\\h+\\k) {\\order};
    \\node[diagsymbolnode] (D2) at (-0.5*\\w+\\k,0.5*\\h-\\k) {\\order};

    \\node[namenode,below = 3pt of north] (N1) {\\name};
    \\node[namenode,above = 3pt of south] (N2) {\\name};

    \\node[valuenode,right = 1pt of west,rotate=90,anchor=north] (V1) {\\value\\magnitude{\\power}\\unit};
    \\node[valuenode,left = 1pt of east,rotate=-90,anchor=north] (V2) {\\value\\magnitude{\\power}\\unit};
    \\node[formulaenode,below = 2pt of N1] (F1) {\\formulae};
    \\node[formulaenode,above = 2pt of N2] (F2) {\\formulae};
\\end{tikzpicture}
\\end{document}
"""
