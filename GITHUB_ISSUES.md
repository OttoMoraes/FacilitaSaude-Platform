# GitHub Issues

## Issue 1: Criar configuração de ambiente segura
**Descrição**
Configurar o projeto para carregar variáveis de ambiente, remover `SECRET_KEY` hardcoded e preparar settings modulares para `development` e `production`.

**Prioridade**: Alta
**Dependências**: `backend/config/settings.py`
**Estimativa**: 1-2 dias

**Checklist**
- [ ] Criar `.env.example`
- [ ] Configurar `python-dotenv` ou `django-environ`
- [ ] Movimentar `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASES` para variáveis de ambiente
- [ ] Adicionar `settings/base.py`, `settings/development.py`, `settings/production.py`

## Issue 2: Implementar app accounts e autenticação
**Descrição**
Criar modelos de usuário e perfil, endpoints de autenticação e views de login/registro.

**Prioridade**: Alta
**Dependências**: `backend/apps/accounts/`, `backend/config/urls.py`
**Estimativa**: 1 semana

**Checklist**
- [ ] Definir modelo `UserProfile`
- [ ] Configurar `AUTH_USER_MODEL` se necessário
- [ ] Criar serializers e views para registro/login
- [ ] Criar admin para gestão de usuários
- [ ] Adicionar testes de autenticação

## Issue 3: Criar app encyclopedia
**Descrição**
Adicionar módulo de enciclopédia de saúde com modelos para artigos, categorias e busca.

**Prioridade**: Média
**Dependências**: `backend/apps/encyclopedia/`
**Estimativa**: 1-2 semanas

**Checklist**
- [ ] Criar app `encyclopedia`
- [ ] Definir modelos de conteúdo
- [ ] Implementar APIs de consulta e busca
- [ ] Criar templates para listagem e detalhe

## Issue 4: Criar estrutura frontend base
**Descrição**
Definir pastas de templates e estáticos, incluir Bootstrap e criar layout base.

**Prioridade**: Média
**Dependências**: `backend/templates/`, `backend/static/`
**Estimativa**: 3 dias

**Checklist**
- [ ] Criar estrutura `templates/base.html`
- [ ] Criar estrutura `static/css/` e `static/js/`
- [ ] Adicionar layout básico com navbar e rodapé
- [ ] Garantir `APP_DIRS = True`

## Issue 5: Documentar roadmap e sprints
**Descrição**
Preencher `docs/03-roadmap/ROADMAP.md` e `docs/09-sprints/SPRINTS.md` com metas e cronograma realistas.

**Prioridade**: Alta
**Dependências**: documentação existente
**Estimativa**: 1-2 dias

**Checklist**
- [ ] Atualizar ROADMAP.md
- [ ] Atualizar SPRINTS.md
- [ ] Alinhar com visão e arquitetura
