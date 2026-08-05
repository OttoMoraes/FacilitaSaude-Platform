# FacilitaSaude Project Status

## Onde estamos?
O projeto está atualmente em uma fase de scaffold inicial. O repositório contém a estrutura básica de um projeto Django, mas não há implementação funcional dos módulos planejados.

## Quão pronto está o projeto?
- Backend: 5% (estrutura inicial do Django e uma app `accounts` vazia)
- Frontend: 0% (sem templates, CSS ou JavaScript)
- Banco de dados: 0% (sem modelos ou migrações aplicáveis)

## Quais módulos estão prontos?
- Apenas a infraestrutura mínima de Django e um app `accounts` criado.

## Quais módulos ainda faltam?
- accounts: falta implementação completa de autenticação e perfil
- encyclopedia
- nutrition
- training/exercises
- mental_health
- emergency
- ai
- dashboard
- notifications
- premium
- data ingestion (`SUS`, `TACO`, `IBGE`)

## Próximo passo recomendado
1. Definir a arquitetura de apps e o layout de pastas.
2. Implementar configuração de ambiente segura (gerenciamento de secrets, `DEBUG`, `ALLOWED_HOSTS`).
3. Criar modelos de usuário e perfil como base do banco.
4. Criar roteamento e endpoints básicos para `accounts`.
5. Estruturar scaffolding para apps planejados.

## Riscos atuais
- Exposição de `SECRET_KEY` e `DEBUG = True` podem causar problemas se o projeto for exposto publicamente.
- Falta de implementação de funcionalidades planejadas dificulta estimativas e priorização.
- Dependências instaladas sem uso podem gerar confusão e dívidas técnicas.
- A ausência de documentação de execução e ambiente impede onboarding rápido.
