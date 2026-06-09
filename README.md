# 📦 Lendify - Sistema de Gerenciamento de Empréstimos

> Sistema web para controle de empréstimos, reservas e devoluções de equipamentos, desenvolvido para facilitar a organização de itens como projetores, notebooks, kits e demais recursos compartilhados.

![React](https://img.shields.io/badge/React-Front--end-61DAFB?style=for-the-badge&logo=react&logoColor=000)
![Django](https://img.shields.io/badge/Django-Back--end-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-Language-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

O **Lendify** é uma plataforma web desenvolvida para gerenciar o processo de reserva, empréstimo e devolução de equipamentos de forma simples, organizada e segura.

O sistema permite que usuários solicitem reservas de equipamentos disponíveis, enquanto operadores e administradores acompanham, aprovam, recusam e registram devoluções, mantendo maior controle sobre o patrimônio e o histórico de movimentações.

---

## 1. Domínio do Problema

Instituições, empresas e ambientes acadêmicos frequentemente possuem equipamentos compartilhados, como notebooks, projetores, cabos, kits e outros recursos utilizados por diferentes pessoas.

Quando esse controle é feito manualmente, podem ocorrer problemas como:

- ❌ Falta de controle sobre quem está com determinado equipamento
- ❌ Reservas duplicadas para o mesmo período
- ❌ Equipamentos não devolvidos no prazo
- ❌ Dificuldade para consultar disponibilidade
- ❌ Ausência de histórico de empréstimos
- ❌ Falta de rastreabilidade nas aprovações e devoluções

O **Lendify** surge como uma solução para centralizar essas informações e tornar o processo de empréstimo mais eficiente.

---

## 2. Objetivo do Projeto

O objetivo do projeto é desenvolver um sistema web para gerenciamento de empréstimos e reservas de equipamentos, permitindo:

- ✅ Consultar equipamentos disponíveis
- ✅ Solicitar reservas
- ✅ Aprovar ou recusar solicitações
- ✅ Registrar retirada e devolução
- ✅ Gerenciar equipamentos cadastrados
- ✅ Controlar usuários e permissões
- ✅ Visualizar histórico e logs do sistema

A proposta é substituir controles manuais por uma aplicação digital organizada, com diferentes perfis de acesso e maior segurança nas operações.

---

## 3. Informações Acadêmicas

| Campo | Informação |
|---|---|
| Projeto | P03-B - Reserva de Equipamentos |
| Disciplina | Segurança da Informação |
| Professor | Edson Vaz Lopes |
| Curso | Engenharia de Software |
| Sistema | Lendify |

---

## 4. Integrantes

- Miguel Angelo Dufloth Filho
- Miguel Angel Balladares Huertas
- Luis Fernando Pereira
- Leonardo Lotério de Lima
- Lucas Honorato dos Santos

---

## 5. Perfis de Usuário

O sistema possui diferentes níveis de acesso, de acordo com a responsabilidade de cada usuário.

### Solicitante

Usuário responsável por solicitar e acompanhar suas próprias reservas.

Funcionalidades previstas:

- Visualizar equipamentos disponíveis
- Solicitar reserva de equipamento
- Acompanhar status das próprias solicitações
- Consultar histórico de empréstimos
- Registrar ou acompanhar devoluções

### Operador

Usuário responsável por controlar o fluxo de empréstimos e devoluções.

Funcionalidades previstas:

- Visualizar solicitações pendentes
- Aprovar reservas
- Recusar reservas
- Registrar retirada de equipamentos
- Registrar devolução
- Consultar equipamentos emprestados

### Administrador

Usuário com controle completo sobre o sistema.

Funcionalidades previstas:

- Gerenciar usuários
- Gerenciar equipamentos
- Consultar logs do sistema
- Visualizar todas as reservas
- Controlar permissões
- Acompanhar histórico geral de movimentações

---

## 6. Principais Funcionalidades

### Gestão de Equipamentos

Permite o cadastro, edição, visualização e controle dos equipamentos disponíveis para empréstimo.

Exemplos de equipamentos:

- Projetores
- Notebooks
- Kits de apresentação
- Cabos e adaptadores
- Equipamentos de apoio

### Reserva de Equipamentos

Permite que o solicitante escolha um equipamento disponível e realize uma solicitação de reserva.

A reserva pode passar por diferentes status, como:

- Pendente
- Aprovada
- Recusada
- Em andamento
- Devolvida
- Cancelada

### Controle de Empréstimos

Após a aprovação da reserva, o operador pode registrar a retirada do equipamento e acompanhar sua devolução.

### Histórico e Logs

O sistema mantém registros das ações realizadas, permitindo maior controle e rastreabilidade.

Exemplos de registros:

- Solicitação criada
- Reserva aprovada
- Reserva recusada
- Equipamento retirado
- Equipamento devolvido
- Alterações administrativas

---

## 7. Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Front-end | React |
| Back-end | Django |
| Linguagem Back-end | Python |
| Banco de Dados | MySQL |
| Controle de Versão | Git e GitHub |

---

## 8. Arquitetura do Sistema

O projeto é dividido em três camadas principais:

```txt
Usuário
  ↓
Front-end React
  ↓
API Back-end Django
  ↓
Banco de Dados MySQL
