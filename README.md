# firebasewebpy
Hola mundo de colección entre firebase y web.py.

## 1. Crear un virtual environment

```zsh
python3 -m venv .venv
```

## 2. Activar un ambiente virtual

```zsh
source '.venv/bin/activate'
```

## 3. Salir de virtual environment 

```zsh
deactivate
```

## 4. Eliminar virtual environment

```zsh
rm -rf /workspaces/webpy/.venv
```

## 5. Actualizar pip

```zsh
pip install --upgrade pip
```

## 6. Instalar librerias

```zsh
pip install web.py requests pyrebase4 setuptools
```

## 7. Crear requirements.txt

```zsh
pip freeze > requirements.txt
```

## 8. Crear el archivo runtime.txt

```zsh
python3 -V > runtime.txt
```