# ToDoApp

ToDoApp es una aplicación web de gestión de tareas simple construida usando **Flask** y **Tailwind CSS**. Permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas con diferentes niveles de prioridad. Los usuarios también pueden adjuntar imágenes a sus tareas y marcarlas como completadas.

## Características

- Sistema de registro e inicio de sesión de usuarios.
- Panel de control para gestionar las tareas.
- Priorización de tareas con diferentes niveles (e.g., baja, media, alta, urgente).
- Adjuntar imágenes a las tareas.
- Seguimiento del estado de las tareas (completadas o no).
- Seguridad integrada con Flask-Login.

## Estructura del proyecto


bash
├── app.py               # Archivo principal de la aplicación
├── config.py            # Configuraciones
├── forms.py             # Formularios WTForms para autenticación y gestión de tareas
├── models.py            # Modelos de SQLAlchemy para usuarios y tareas
├── routes/              # Blueprints de Flask para autenticación y tareas
│   ├── auth.py          # Rutas para login, registro y logout
│   ├── tasks.py         # Rutas para gestión de tareas
├── static/              # Archivos estáticos (e.g., CSS, imágenes)
├── templates/           # Plantillas HTML
├── venv/                # Entorno virtual de Python
├── data/                # Ubicación de la base de datos SQLite
├── README.md            # Documentación del proyecto (este archivo)
├── requirements.txt     # Dependencias del proyecto
└── .gitignore           # Archivo para ignorar archivos sensibles y no necesarios

# Requisitos
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Tailwind CSS

# Instalación

Clona el repositorio:

bash
git clone 
cd todoapp

Configura un entorno virtual:
python -m venv venv
source venv/bin/activate   # Para Linux/MacOS
venv\Scripts\activate      # Para Windows

Instala las dependencias:
pip install -r requirements.txt

Ejecuta la aplicación Flask:
python app.py
