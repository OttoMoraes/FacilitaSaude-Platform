# FacilitaSaude Roadmap

## Sprint 1 — Foundation and Environment
- Objetivo: Estabelecer a base do projeto e preparar um ambiente seguro e configurável.
- Arquivos envolvidos:
  - `backend/config/settings.py`
  - `backend/manage.py`
  - `backend/requirements/base.txt`
  - `README.md`
  - `PROJECT_STATUS.md`
- Banco: Configuração de base para PostgreSQL via variáveis de ambiente.
- Backend: Criar settings modulares e start do app `accounts`.
- Frontend: Definir estrutura básica de templates e estáticos.
- Testes: Validar migrações e execução do servidor.
- Tempo estimado: 1-2 semanas.
- Complexidade: Média.
- Dependências: Definição de variáveis de ambiente e guidance de deploy.

## Sprint 2 — Usuários e Autenticação
- Objetivo: Implementar o núcleo de autenticação e perfis de usuário.
- Arquivos envolvidos:
  - `backend/apps/accounts/models.py`
  - `backend/apps/accounts/views.py`
  - `backend/apps/accounts/admin.py`
  - `backend/apps/accounts/tests.py`
  - `backend/config/urls.py`
- Banco: Criar modelos `UserProfile` e possíveis extensões de usuário.
- Backend: APIs e views para registro, login e perfil.
- Frontend: Templates de login, registro e dashboard inicial.
- Testes: Cobertura dos endpoints de autenticação e modelos.
- Tempo estimado: 2 semanas.
- Complexidade: Média.
- Dependências: Configuração de ambiente, esquema de usuários.

## Sprint 3 — Conteúdo e Enciclopédia
- Objetivo: Implementar a enciclopédia de saúde e consultas de conteúdo.
- Arquivos envolvidos:
  - `backend/apps/encyclopedia/`
  - `backend/apps/encyclopedia/models.py`
  - `backend/apps/encyclopedia/views.py`
  - `backend/apps/encyclopedia/serializers.py`
  - `backend/config/settings.py`
- Banco: Modelos para artigos, tags e categorias.
- Backend: API REST para pesquisa e leitura de conteúdo.
- Frontend: Templates de listagem e detalhe de artigos.
- Testes: Documentação e cobertura de consultas de conteúdo.
- Tempo estimado: 2 semanas.
- Complexidade: Média.
- Dependências: Base de usuários e definição de conteúdo.

## Sprint 4 — Nutrição, Exercícios e Dashboard
- Objetivo: Implementar módulos de nutrição e treino com dashboard inicial.
- Arquivos envolvidos:
  - `backend/apps/nutrition/`
  - `backend/apps/training/`
  - `backend/apps/dashboard/`
- Banco: Modelos para alimentação, refeições, exercícios e métricas.
- Backend: CRUD e APIs para dados de saúde e atividades.
- Frontend: Interface de dashboard com gráficos básicos.
- Testes: Validar modelos e lógica de média/metas.
- Tempo estimado: 3 semanas.
- Complexidade: Alta.
- Dependências: Usuários autenticados e estrutura de dados.

## Sprint 5 — IA, Saúde Mental e Premium
- Objetivo: Adicionar assistente AI, módulo de saúde mental e arquitetura de Premium.
- Arquivos envolvidos:
  - `backend/apps/ai/`
  - `backend/apps/mental_health/`
  - `backend/apps/notifications/`
  - `backend/apps/emergency/`
- Banco: Modelos para histórico mental, avaliações e planos premium.
- Backend: Integração com IA, notificações e permissões premium.
- Frontend: Fluxo de conversas, alertas e oferta de recurso premium.
- Testes: Cobertura de segurança e integração de IA.
- Tempo estimado: 4 semanas.
- Complexidade: Alta.
- Dependências: Infraestrutura de API, autenticação e modelagem de dados.
