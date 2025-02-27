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
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------

project = "ProtoTorch"
copyright = "2021, Jensun Ravichandran"
author = "Jensun Ravichandran"

# The full version, including alpha/beta/rc tags
#
release = "0.4.4"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "1.6"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "sphinxcontrib.katex",
]

# katex_prerender = True
katex_prerender = False

napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use. Choose from:
# ["default", "emacs", "friendly", "colorful", "autumn", "murphy", "manni",
#  "monokai", "perldoc", "pastie", "borland", "trac", "native", "fruity", "bw",
#  "vim", "vs", "tango", "rrt", "xcode", "igor", "paraiso-light", "paraiso-dark",
#  "lovelace", "algol", "algol_nu", "arduino", "rainbo w_dash", "abap",
#  "solarized-dark", "solarized-light", "sas", "stata", "stata-light",
#  "stata-dark", "inkpot"]
pygments_style = "monokai"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Disable docstring inheritance
autodoc_inherit_docstrings = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# https://sphinx-themes.org/
html_theme = "sphinx_rtd_theme"

html_logo = "_static/img/horizontal-lockup.png"

html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#ffffff",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css",
]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "protoflowdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    #
    # "papersize": "letterpaper",
    # The font size ("10pt", "11pt" or "12pt").
    #
    # "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    #
    # "preamble": "",
    # Latex figure (float) alignment
    #
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "prototorch.tex",
        "ProtoTorch Documentation",
        "Jensun Ravichandran",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "ProtoTorch", "ProtoTorch Documentation", [author],
              1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "prototorch",
        "ProtoTorch Documentation",
        author,
        "prototorch",
        "Prototype-based machine learning in PyTorch.",
        "Miscellaneous",
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
}

# -- Options for Epub output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-epub-output

epub_cover = ()
version = release
