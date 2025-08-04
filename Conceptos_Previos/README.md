# Comandos
```
python --version
git --version
https://git-scm.com/downloads/win
pip list
python.exe -m pip install --upgrade pip
pip install pandas
```
## Crear entorno virtual
python -m venv env
## Activar entorno
env\scripts\activate
Si no se activa, usar este comando en PowerShell
set-ExecutionPolicy Unrestricted
y escriba "S"

## Estructuras de datos en Pandas
| Tipo      | Contenido                                      |
| --------- | ---------------------------------------------- |
| Series    | Array de una dimensión                         |
| DataFrame | Se corresponde con unas tabla de 2 dimensiones |
| Panel     | Similar a un diccionario de DataFrame          |

Alt + shift + f

# Creación de objetos Series
```
import pandas as pd # pip install pandas
# Creación de objeto Serie
s = pd.series([2,4,6,8,10])
print(s)

```
manejo de git
git init #inicializa el repositorio
git add .
git commit -m "introducción a pandas 5%"
si sale error
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

crear archivo requeriments.txt
pip freeze > requirements.txt
clonar repositorio
https://github.com/michellegallegoabril/CURSO_IA.git
como desactivar el entorno virtual: deactivate