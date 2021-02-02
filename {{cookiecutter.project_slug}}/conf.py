# -- Project information
project = "{{ cookiecutter.project_slug }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
release = "{{ cookiecutter.release }}"

# -- General configuration
language = "en"
extensions = [
    "sphinx_revealjs",
]
template_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv"]

# -- Options for Revealjs output
revealjs_static_path = ["_static"]
revealjs_style_theme = "{{ cookiecutter.style_theme }}"
