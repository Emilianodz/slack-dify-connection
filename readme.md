# Mi Proyecto Django

Este es un proyecto desarrollado con Django, un framework web de Python. Si vienes de Flask, encontrarás algunas similitudes y diferencias interesantes.

## Requisitos Previos

- Python 3.8+
- pip (gestor de paquetes de Python)
- virtualenv (recomendado)

## Instalación

1. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
mi_proyecto/
├── manage.py              # Equivalente al app.py en Flask
├── requirements.txt
├── mi_proyecto/          # Configuración principal (similar a config.py en Flask)
│   ├── __init__.py
│   ├── settings.py       # Configuraciones (DEBUG, DATABASE, etc.)
│   ├── urls.py          # Rutas principales (similar a @app.route en Flask)
│   └── wsgi.py
└── mi_app/              # Tu aplicación (similar a un Blueprint en Flask)
    ├── __init__.py
    ├── admin.py         # Configuración del panel admin
    ├── apps.py
    ├── models.py        # Modelos de base de datos (similar a Models en Flask-SQLAlchemy)
    ├── views.py         # Vistas (similar a las rutas en Flask)
    └── templates/       # Templates HTML
```

## Diferencias Principales con Flask

1. **Rutas (URLs)**
   - Flask: `@app.route('/ruta')`
   - Django: Se definen en `urls.py` usando `path('ruta/', vista)`

2. **Vistas**
   - Flask: Funciones decoradas
   - Django: Clases basadas en vistas o funciones en `views.py`

3. **Templates**
   - Flask: `{{ variable }}`
   - Django: Similar, pero con más filtros y tags incorporados

4. **Modelos**
   - Flask: Flask-SQLAlchemy
   - Django: ORM incorporado en `models.py`

## Comandos Básicos

# Crear migraciones (similar a flask db migrate)
python manage.py makemigrations

# Aplicar migraciones (similar a flask db upgrade)
python manage.py migrate

# Crear superusuario para el admin
python manage.py createsuperuser

# Iniciar servidor de desarrollo
python manage.py runserver

## Desarrollo

1. Crea modelos en `models.py`
2. Crea vistas en `views.py`
3. Define URLs en `urls.py`
4. Crea templates en la carpeta `templates`

