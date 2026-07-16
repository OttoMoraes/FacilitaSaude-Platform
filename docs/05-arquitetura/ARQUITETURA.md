# Arquitetura do Sistema - FacilitaSaúde

## Objetivo

A arquitetura do FacilitaSaúde foi projetada para ser modular, organizada e escalável, permitindo que novos recursos sejam adicionados sem comprometer a estrutura existente.

---

# Arquitetura em Camadas

Usuário
↓
Frontend
↓
API Django REST
↓
Serviços
↓
Banco de Dados

---

# Organização dos Apps

Cada grande módulo do sistema será um aplicativo Django independente.

Os módulos previstos são:

- accounts
- encyclopedia
- nutrition
- mental_health
- training
- emergency
- ai
- dashboard
- notifications

---

# Objetivo

Cada módulo será responsável apenas por sua própria regra de negócio, facilitando manutenção, testes e evolução do sistema.
