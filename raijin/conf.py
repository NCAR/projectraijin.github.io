#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import datetime
import shutil


# -- Project information -----------------------------------------------------

project = 'Project Raijin'
author = 'Project Raijin Developers & Contributors'
copyright = f'2021-{datetime.datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Define what extensions will parse which kind of source file
source_suffix = '.rst'

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    html_theme = 'default'
else:
    import sphinx_bootstrap_theme
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# # Logo & Title
# html_logo = '_static/images/logos/GeoCAT_Final_Logos-01.svg'
# html_title = ''

# # Favicon
# html_favicon = '_static/images/icons/favicon.ico'

# # Permalinks Icon
# html_permalinks_icon = '<i class="bi bi-link"></i>'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_css_files = ['custom.css']
# html_js_files = ['custom.js']

# # HTML Theme-specific Options
# html_theme_options = {
#     'onepagers': [
#         'index',
#     ],
#     'logos_bar': {
#         'NCAR': '/_static/images/logos/NCAR-contemp-logo-blue.svg',
#         'Unidata': '/_static/images/logos/Unidata_logo_horizontal_1200x300.svg',
#         'UAlbany': '/_static/images/logos/UAlbany-A2-logo-purple-gold.svg',
#     },
#     'sponsor_text': 'This material is based upon work supported by the National Science Foundation under Grant Nos. 2026863 and 2026899. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.',
#     'sponsor_logo': '/_static/images/logos/footer-logo-nsf.png',
# }

# # Disable sidebars on all pages
# html_sidebars = {
#     '**': [],
# }

# # Panels config
# panels_add_bootstrap_css = False

# CUSTOM SCRIPTS ==============================================================

# Copy root files into content pages ------------------------------------------

