# FacilitaSaude Final Report

## Situação atual
O projeto está em estágio de protótipo de scaffold. Há a base de um projeto Django, mas nenhum dos módulos de negócio planejados foi implementado.

## Funcionalidades prontas
- Criação do projeto Django.
- App `apps.accounts` existente como scaffold.
- Configuração inicial em `backend/config/settings.py`.

## Funcionalidades parcialmente prontas
- Estrutura de projeto e documentação inicial.
- Dependências definidas em `backend/requirements/base.txt`.

## Funcionalidades futuras
- Sistema de usuários completo.
- Enciclopédia de saúde.
- Nutrição e alimentação.
- Exercícios e treino.
- Saúde mental.
- Assistente IA.
- Dashboard.
- Módulo premium.
- Integração de dados SUS/TACO/IBGE.
- Notificações.

## Arquitetura
A visão original prevê uma arquitetura modular por apps Django e camadas de frontend, API, serviços e banco de dados. O código atual não reflete essa arquitetura, pois apenas um app está presente.

## Banco
O planejamento indica PostgreSQL e módulos de dados independentes. O código atual usa SQLite e não possui nenhum modelo ou migração além de `__init__.py`.

## Fluxo da aplicação
Planejado: usuário → frontend → API REST → serviços → banco.
Implementado: apenas o esqueleto Django com rota de admin.

## Próximos passos
1. Implementar configuração de ambiente segura.
2. Estruturar app `accounts` com autenticação básica.
3. Criar os apps planejados `encyclopedia`, `nutrition`, `training`, `mental_health`, `ai`, `dashboard`, `notifications`.
4. Estabelecer templates e static.

## Dívida técnica
- Hardcoded `SECRET_KEY` e `DEBUG = True`.
- Dependências sem uso (`djangorestframework`, `python-dotenv`).
- Planos documentados sem implementação.
- Ausência de testes e migrações.
