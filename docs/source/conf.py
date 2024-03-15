# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../lambda_functions/student'))
sys.path.insert(0, os.path.abspath('../../lambda_functions/teacher'))
sys.path.insert(0, os.path.abspath('../../lambda_functions/admin'))
sys.path.insert(0, os.path.abspath('../../lambda_functions/course'))
sys.path.insert(0, os.path.abspath('../../lambda_functions/department'))
sys.path.insert(0, os.path.abspath('../../lambda_functions/cognito'))

sys.path.insert(0, os.path.abspath('../../tests/test_student'))
sys.path.insert(0, os.path.abspath('../../tests/test_teacher'))
sys.path.insert(0, os.path.abspath('../../tests/test_admin'))
sys.path.insert(0, os.path.abspath('../../tests/test_course'))
sys.path.insert(0, os.path.abspath('../../tests/test_department'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Attendance System'
copyright = '2024, DevOps Group 6'
author = 'DevOps Group 6'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
