# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'aRTist Handbook'
copyright = '2021-2022, Bundesanstalt für Materialforschung und -prüfung (BAM)'
author = 'BAM, Bundesanstalt für Materialforschung und -prüfung'

# The full version, including alpha/beta/rc tags
release = '2.12'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Bibliography extension available from:
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/quickstart.html
extensions = [
	"sphinx_rtd_theme",
	"sphinx.ext.autosectionlabel",
	"sphinxcontrib.bibtex",
	"sphinx.ext.imgmath",   # to render equations as PNG images and avoid externally loaded JavaScript libraries
    # for exclude part of documents
	#'sphinx_selective_exclude.eager_only',
    #'sphinx_selective_exclude.search_auto_exclude',
    #'sphinx_selective_exclude.modindex_exclude',
]

# Add the path of a bibliography (.bib) file
bibtex_bibfiles = ['references.bib']

# Define bibtex enconding (default: utf-8-sig)
bibtex_encoding = 'utf-8-sig'

# Define bibtex style
bibtex_default_style = 'unsrt'

imgmath_latex_preamble = """\\usepackage{sansmathfonts}
\\usepackage{amsmath, amssymb}"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Change autoconfigextension default behaviour for section labels, in order to
# avoid duplicate label summary warnings.
# Source: https://www.spinics.net/lists/linux-doc/msg77015.html
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 1

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Figures with numbers:
numfig = True
numfig_format = {
	"figure":     "Fig. %s",
	"table":      "Tab. %s",
	"code-block": "Listing %s",
	"section":    "Sec. %s"
}

# Our own global roles (commands accesible in all .rst files):
rst_prolog = """
.. |nbsp| unicode:: 0xA0
    :trim:
.. |artist| replace:: *aRT*\\ ist
"""
# The html index document.
master_doc = 'index'

# The latex index document
latex_doc = 'index_latex'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Copyright is handled by extra footer - _templates/footer.html
html_show_copyright = False

# -- Options for LaTeX output -------------------------------------------------
latex_engine = 'pdflatex'
latex_toplevel_sectioning = 'chapter'  # part, section or chapter

# to take index_latex as index for the latexPDF
latex_documents = [
  (latex_doc, 'artisthandbook.tex', project,
   author, 'manual'),
]

latex_elements = {
	'papersize': 'a4paper',
	'pointsize': '11pt',
	'fontpkg': r'''
		\usepackage{PTSans}
		\usepackage{charter}
	''',
	'preamble': r"""
		%% %add number to subsubsection 2=subsection, 3=subsubsection
		\setcounter{secnumdepth}{3}
		%% %% Table of content upto 2=subsection, 3=subsubsection
		\setcounter{tocdepth}{1}
        %% Force table of contents onto one page
        %%\addtocontents{toc}{\protect\enlargethispage{1\normalbaselineskip}}
        
        %% Default title headings of document class Book Chapter one... is deleted
		\usepackage{titlesec}
		\titleformat{\chapter}[display]
  		{\normalfont\bfseries}{}{0pt}{\Huge}

        % package for eps-figures  
		\usepackage{epstopdf}
      
		% background in title
		\usepackage{wallpaper}

      	\usepackage{newunicodechar}
		\newunicodechar{≤}{\ensuremath{\leq}}
		\newunicodechar{≥}{\ensuremath{\geq}}
		\newunicodechar{⋅}{\ensuremath{\cdot}}
		\newunicodechar{≈}{\ensuremath{\approx}}
		\newunicodechar{×}{\ensuremath{\times}}
		\newunicodechar{→}{\ensuremath{\rightarrow}}

		\newunicodechar{α}{\ensuremath{\alpha}}
		\newunicodechar{β}{\ensuremath{\beta}}
		\newunicodechar{γ}{\ensuremath{\gamma}}
		\newunicodechar{δ}{\ensuremath{\delta}}
		\newunicodechar{ϵ}{\ensuremath{\epsilon}}
		\newunicodechar{ε}{\ensuremath{\varepsilon}}
		\newunicodechar{ζ}{\ensuremath{\zeta}}
		\newunicodechar{η}{\ensuremath{\eta}}
		\newunicodechar{θ}{\ensuremath{\theta}}
		\newunicodechar{ϑ}{\ensuremath{\vartheta}}
		\newunicodechar{ι}{\ensuremath{\iota}}
		\newunicodechar{κ}{\ensuremath{\kappa}}
		\newunicodechar{λ}{\ensuremath{\lambda}}
		\newunicodechar{μ}{\ensuremath{\mu}}
		\newunicodechar{ν}{\ensuremath{\nu}}
		\newunicodechar{ξ}{\ensuremath{\xi}}
		\newunicodechar{π}{\ensuremath{\pi}}
		\newunicodechar{ρ}{\ensuremath{\rho}}
		\newunicodechar{σ}{\ensuremath{\sigma}}
		\newunicodechar{τ}{\ensuremath{\tau}}
		\newunicodechar{υ}{\ensuremath{\upsilon}}
		\newunicodechar{φ}{\ensuremath{\phi}}
		\newunicodechar{ϕ}{\ensuremath{\varphi}}
		\newunicodechar{χ}{\ensuremath{\chi}}
		\newunicodechar{ψ}{\ensuremath{\psi}}
		\newunicodechar{ω}{\ensuremath{\omega}}

		\newunicodechar{Γ}{\ensuremath{\Gamma}}
		\newunicodechar{Δ}{\ensuremath{\Delta}}
		\newunicodechar{Θ}{\ensuremath{\Theta}}
		\newunicodechar{Λ}{\ensuremath{\Lambda}}
		\newunicodechar{Ξ}{\ensuremath{\Xi}}
		\newunicodechar{Π}{\ensuremath{\Pi}}
		\newunicodechar{Σ}{\ensuremath{\Sigma}}
		\newunicodechar{ϒ}{\ensuremath{\Upsilon}}
		\newunicodechar{Φ}{\ensuremath{\Phi}}
		\newunicodechar{Ψ}{\ensuremath{\Psi}}
		\newunicodechar{Ω}{\ensuremath{\Omega}}
	""",
    
    'maketitle': r'''
    	\pagenumbering{Roman} %% % to avoid page 1 conflict with actual page 1
	 	\begin{titlepage}
         		\ThisLRCornerWallPaper{1}{artistHandbook.eps}  
                 \mbox{} \thispagestyle{empty}
	 	\end{titlepage}
    '''
}
