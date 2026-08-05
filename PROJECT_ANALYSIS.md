# FacilitaSaude Project Analysis

## Overview
FacilitaSaude is a Django-based health platform in early development. The backend is located in the `backend/` folder. The project currently contains one Django application: `apps.accounts`.

## Project structure

- `LICENSE`
- `README.md`
- `backend/`
  - `manage.py`
  - `config/`
    - `__init__.py`
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`
  - `apps/`
    - `accounts/`
      - `__init__.py`
      - `admin.py`
      - `apps.py`
      - `models.py`
      - `tests.py`
      - `views.py`
  - `requirements/`
    - `base.txt`
- `docs/`
  - `01-visao-projeto/VISAO_PROJETO.md`
  - `02-plano-mestre/PLANO_MESTRE.md`
  - `03-roadmap/ROADMAP.md`
  - `05-arquitetura/ARQUITETURA.md`
  - `06-banco-dados/MODELO_BANCO_DADOS.md`
  - `09-sprints/SPRINTS.md`

## App structure

### `apps.accounts`
- `admin.py` — placeholder register file.
- `apps.py` — application configuration.
- `models.py` — empty, no models defined.
- `tests.py` — placeholder, no tests defined.
- `views.py` — placeholder, no views defined.

## Configuration and settings

### `backend/config/settings.py`
- `BASE_DIR` is configured correctly.
- `SECRET_KEY` is hardcoded: `django-insecure-0x02qn_&0qp$wv6#5ctv-6hswnq)9#$vkqkah$l)#_&zgqudko`.
- `DEBUG = True`.
- `ALLOWED_HOSTS = []`.
- Installed apps include default Django apps plus `apps.accounts`.
- Middleware includes standard Django middleware.
- `ROOT_URLCONF = "config.urls"`.
- Templates use `APP_DIRS = True` and include `request`, `auth`, and `messages` context processors.
- `DATABASES` uses SQLite with `db.sqlite3` in `BASE_DIR`.
- Password validators are standard Django validators.
- `LANGUAGE_CODE = "en-us"`, `TIME_ZONE = "UTC"`, `USE_I18N = True`, `USE_TZ = True`.
- `STATIC_URL = "static/"`.

### `backend/config/urls.py`
- Only includes Django admin route: `path("admin/", admin.site.urls)`.

### `backend/manage.py`
- Default Django manage script configured with `config.settings`.

## Dependencies

### `backend/requirements/base.txt`
- `asgiref==3.12.1`
- `Django==6.0.7`
- `djangorestframework==3.17.1`
- `python-dotenv==1.2.2`
- `sqlparse==0.5.5`

## Models
- No model definitions exist in `backend/apps/accounts/models.py`.

## Views
- No view definitions exist in `backend/apps/accounts/views.py`.

## URLs
- No application-level URL configuration exists.
- Global URL configuration only exposes admin.

## Templates
- No template directories or template files found.
- `TEMPLATES[0]["DIRS"]` is empty.

## Static files
- No static file directories detected in the workspace.

## Migrations and database
- No migration files exist in `backend/apps/accounts/migrations/` aside from `__init__.py`.
- Database is configured for SQLite but no actual migrations are present.

## Environment variables
- No `.env` or environment-specific settings files exist.
- `python-dotenv` is installed, but not used in settings.

## Project documentation
- Existing docs are present under `docs/` with higher-level planning content.
- README is minimal and does not reflect current backend status.

## Summary
The current repository is a scaffold for a Django platform with a single app and placeholder files. Core business logic, templates, static assets, app routing, models, and views are not implemented yet. The project requires architectural organization, documentation, and completion of planned features.
