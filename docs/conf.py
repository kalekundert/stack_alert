import sys, os
import stack_alert

## General

project = 'Stack Alert'
copyright = '2020, Kale Kundert'
version = stack_alert.__version__
release = stack_alert.__version__

master_doc = 'index'
source_suffix = '.rst'
templates_path = ['_templates']
exclude_patterns = ['_build']
default_role = 'any'

## Extensions

extensions = [
        'autoclasstoc',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.viewcode',
        'sphinx.ext.intersphinx',
        'sphinx_rtd_theme',
]
intersphinx_mapping = { #
}
autosummary_generate = True
autodoc_default_options = {
        'exclude-members': '__dict__,__weakref__,__module__',
}
html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']
pygments_style = 'sphinx'

