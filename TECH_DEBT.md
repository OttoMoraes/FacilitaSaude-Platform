# FacilitaSaude Technical Debt

## Current debt items

### 1. Missing core implementation
- No models, serializers, views, or URLs for planned modules.
- No frontend templates or static assets.
- No migration history or database schema.

### 2. Security and configuration debt
- Hardcoded `SECRET_KEY`.
- `DEBUG = True` in production settings.
- `ALLOWED_HOSTS` not configured.
- `python-dotenv` dependency unused.
- No environment segmentation or secrets management.

### 3. Architectural debt
- Plan describes modular architecture, but code has only one app.
- No service or layer separation for business logic.
- No API scaffolding despite DRF dependency.
- No documentation of execution or environment setup.

### 4. Documentation debt
- Empty roadmap and sprint documents.
- Minimal README.
- No onboarding or developer guide.

### 5. Dependecy debt
- `djangorestframework` installed and unused.
- `python-dotenv` installed and unused.
- No lock file or dependency management beyond `base.txt`.

## Impact
- Slows onboarding and development.
- Increases the risk of architectural rework.
- Makes production deployment unsafe.
- Creates uncertainty around feature priorities.

## Suggested remediation
1. Stabilize configuration and environment management.
2. Implement the accounts module as a foundation.
3. Define app boundaries and bootstrap planned modules.
4. Add basic tests and documentation for setup.
5. Remove or justify unused dependencies once feature work begins.
