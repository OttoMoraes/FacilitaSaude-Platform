# FacilitaSaude Project Structure

## Repositório atual

- `LICENSE`
- `README.md`
- `PROJECT_ANALYSIS.md`
- `PROJECT_STATUS.md`
- `PROJECT_STRUCTURE.md`
- `FEATURE_MATRIX.md`
- `ERROR_REPORT.md`
- `TECH_DEBT.md`
- `NEXT_STEPS.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `GITHUB_ISSUES.md`
- `KANBAN_BOARD.md`
- `backend/`
  - `manage.py` — Django CLI entrypoint.
  - `config/` — Django project configuration.
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

## Observações de estrutura
- Arquitetura modular está planejada, mas não refletem no código.
- Não existem diretórios típicos para `templates/`, `static/`, `services/`, `serializers/`, `permissions/`, `tests/` dedicados ou `docs/` de implementação.
- A única app criada é `apps.accounts`.
- Não há `migrations/` com modelos implementados.

## Recomendações de estrutura futura
- Criar diretórios globais em `backend/` para:
  - `templates/`
  - `static/`
  - `services/`
  - `serializers/`
  - `permissions/`
  - `validators/`
  - `mixins/`
  - `forms/`
  - `signals/`
- Organizar `apps/` como apps Django independentes:
  - `apps.accounts`
  - `apps.encyclopedia`
  - `apps.nutrition`
  - `apps.training`
  - `apps.mental_health`
  - `apps.emergency`
  - `apps.ai`
  - `apps.dashboard`
  - `apps.notifications`
- Estruturar `config/settings/` com `base.py`, `development.py`, `production.py` e `local.py`.
- Adicionar `requirements/` com `dev.txt` e `prod.txt`.
