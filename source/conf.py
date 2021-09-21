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

project = 'aRTist'
copyright = '2021, BAM, Bundesanstalt für Materialforschung und -prüfung'
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
	"sphinxcontrib.bibtex"
]

# Add the path of a bibliography (.bib) file
bibtex_bibfiles = ['references.bib']

# Define bibtex enconding (default: utf-8-sig)
bibtex_encoding = 'latin'

# Define bibtex style
bibtex_default_style = 'unsrt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
"""


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


# -- Options for LaTeX output -------------------------------------------------
latex_engine = 'pdflatex'
latex_toplevel_sectioning = 'chapter'  # part, section or chapter
latex_elements = {
	'papersize': 'a4paper',
	'pointsize': '11pt',
	'fontpkg': r'''
		\usepackage{ptsans}
		\usepackage{charter}
	''',
	'preamble': r"""
		\usepackage{newunicodechar}
		\newunicodechar{≤}{\ensuremath{\leq}}
		\newunicodechar{≥}{\ensuremath{\geq}}
		\newunicodechar{ρ}{\ensuremath{\rho}}
		\newunicodechar{π}{\ensuremath{\pi}}
		\newunicodechar{⋅}{\ensuremath{\cdot}}
		\newunicodechar{≈}{\ensuremath{\approx}}
	"""
}
