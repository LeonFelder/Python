import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""
letra = input('Ingrese una letra: ')
if letra in string.ascii_letters:
    for elem in jupyter_info.split():
        if  elem.strip().lower().startswith(letra):
            print(elem.strip())
else:
    print("Eso no es una letra")