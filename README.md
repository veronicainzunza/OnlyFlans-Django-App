# OnlyFlans - Proyecto Django

Aplicación web desarrollada con Django que permite visualizar y administrar productos tipo flan.
Incluye panel de administración, manejo de usuarios y renderizado de vistas dinámicas.

---

## Tecnologías utilizadas

* Python
* Django
* Bootstrap 5
* SQLite
* django-crispy-forms

---

## Estructura del proyecto

* `onlyflans/` → configuración principal del proyecto
* `web/` → aplicación principal
* `templates/` → vistas HTML
* `db.sqlite3` → base de datos local (no incluida en el repositorio)

---

## Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

```bash
# Clonar repositorio
git clone https://github.com/TU-USUARIO/TU-REPO.git

# Entrar al proyecto
cd TU-REPO

# Crear entorno virtual
python -m venv venv

# Activar entorno (Git Bash)
source venv/Scripts/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver
```

Luego abre en tu navegador:

http://127.0.0.1:8000/

---

## Panel de administración

Accede a:

http://127.0.0.1:8000/admin/

Para crear un usuario administrador:

```bash
python manage.py createsuperuser
```

---

## Base de datos

Este proyecto utiliza SQLite como base de datos por defecto.

El archivo `db.sqlite3` no se incluye en el repositorio.
Para generar la base de datos desde cero:

```bash
python manage.py migrate
```

---

## Funcionalidades

* Visualización de productos
* Panel de administración Django
* Gestión de usuarios
* Formularios con django-crispy-forms
* Diseño responsive con Bootstrap

---

## Notas

* Este proyecto está configurado para entorno de desarrollo (`DEBUG = True`)
* No está preparado para producción
* Se recomienda usar variables de entorno para datos sensibles

---

## Autor

Proyecto desarrollado por Verónica Inzunza

---
