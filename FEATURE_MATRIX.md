# FacilitaSaude Feature Matrix

## Comparison: Planned vs Implemented

| Funcionalidade | Planejada | Implementada | Status | Observações |
|---|---|---|---|---|
| Sistema de usuários | ✔ | Parcial | Estrutura inicial | `accounts` app existe, mas sem modelos ou views. Django auth está presente apenas por padrão. |
| Enciclopédia | ✔ | ❌ | Não iniciada | Sem app, sem modelos, sem rotas, sem conteúdo. |
| Nutrição | ✔ | ❌ | Não iniciada | Planejado, mas não implementado. |
| Exercícios / Treinos | ✔ | ❌ | Não iniciada | Planejado, mas não implementado. |
| Saúde Mental | ✔ | ❌ | Não iniciada | Planejado, mas não implementado. |
| Assistente IA | ✔ | ❌ | Não iniciada | Planejado, sem código nem integração. |
| Dashboard | ✔ | ❌ | Não iniciada | Planejado, sem painel. |
| Notificações | ✔ | ❌ | Não iniciada | Módulo planejado, não existente. |
| Emergências | ✔ | ❌ | Não iniciada | Módulo planejado, não existente. |
| Dados SUS / TACO / IBGE | ✔ | ❌ | Não iniciada | Planejado como fonte de dados, sem implementação. |
| Premium | ✔ | ❌ | Não iniciada | Planejado no roadmap, não implementado. |
| API Django REST | ✔ | ❌ | Não iniciada | DRF está instalado, mas não há endpoints. |
| Frontend / Templates | ✔ | ❌ | Não iniciada | Não existem templates ou arquivos estáticos. |
| Banco de dados PostgreSQL | ✔ | ❌ | Não implementado | Settings usam SQLite e não há migrações. |
| Configuração de ambiente | ✔ | ❌ | Não implementada | `python-dotenv` não é utilizado. |
| Segurança de produção | ✔ | ❌ | Não implementada | `DEBUG` ativo e `SECRET_KEY` embutido. |

## Status Summary
- Funcionalidades prontas: nenhuma funcional.
- Funcionalidades parcialmente prontas: sistema de usuários em nível de scaffold.
- Funcionalidades faltando: todas as aplicações de domínio planejadas e a infraestrutura de frontend/backend.
