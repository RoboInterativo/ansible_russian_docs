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
import sys
import os

project = "Basic Sphinx Example Project"
copyright = "2022, Read the Docs core team"
author = "Read the Docs core team"


# -- General configuration ---------------------------------------------------
# -- General configuration

sys.path.append(os.path.abspath(os.path.join('.', '_extensions')))


extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    'pygments_lexer',
]



intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
highlight_language = 'YAML+Jinja'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_context = {
#     'display_github': 'True',
#     'github_user': 'ansible',
#     'github_repo': 'ansible',
#     'github_version': 'devel/docs/docsite/rst/',
#     'github_module_version': 'devel/lib/ansible/modules/',
#     'github_root_dir': 'devel/lib/ansible',
#     'github_cli_version': 'devel/lib/ansible/cli/',
#     'current_version': 2.9,
#     'latest_version': '2.9',
#     # list specifically out of order to make latest work
#     'available_versions': ('latest', '2.9', 'devel'),
#     'css_files': ('_static/style.css',  # overrides to the standard theme
#                   ),
# }
