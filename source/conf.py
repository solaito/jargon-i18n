import os
import re
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'jargon-i18n'
copyright = '2024, Original Maintainer: Eric S. Raymond, Converted by @solaito'
author = 'Original Maintainer: Eric S. Raymond, Converted by @solaito'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx_multitoc_numbering",
  'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_context = {
  'current_version' : "latest",
  'versions' : [["latest", "link to latest"]],
  'current_language': 'en',
  'languages': [["en", "link to en"], ["ja", "link to ja"]],
  'display_github': True, # Integrate GitHub
  'github_user': "solaito", # Username
  'github_repo': "jargon-i18n", # Repo name
  'github_version': "develop", # Version
  'conf_py_path': "/source/", # Path in the checkout to the docs root
}


gettext_compact = False

language = 'en'

locale_dir = ['locale/']


def modify_html(app, exception):
	if exception is None:  # ビルドが成功した場合のみ実行
		html_dir = os.path.join(app.outdir)
		for root, dirs, files in os.walk(html_dir):
			for file in files:
				if file.endswith('.html'):
					file_path = os.path.join(root, file)
					with open(file_path, 'r', encoding='utf-8') as f:
						content = f.read()
						# ここでHTML内容の変更を行う
						# 例：特定のタグを置換
					modified_content = re.sub(r'MARKER_REPLACE_WHITE_SPACE', '&nbsp;', content)
					with open(file_path, 'w', encoding='utf-8') as f:
						f.write(modified_content)

def setup(app):
    app.connect('build-finished', modify_html)
