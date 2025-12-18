#  Desafio – Sistema Bancário Simples (Python) da DIO

Este projeto é um **sistema bancário simples em Python**, desenvolvido como exercício prático para treinar conceitos fundamentais da linguagem, como:

- Funções
- Estruturas condicionais
- Laços de repetição
- Listas e dicionários
- Controle de fluxo
- Regras de negócio

O sistema funciona via **terminal**, utilizando um menu interativo.

---

## Arquivo

- `desafio.py` → arquivo principal que contém toda a lógica do sistema

---

## Funcionalidades

O sistema permite:

-  **Depositar valores**
  
-  **Realizar saques**
  - Limite de valor por saque
  - Limite diário de saques
    
-  **Visualizar extrato**
  - Histórico de depósitos e saques
  - Saldo atual
  - Listagem de usuários cadastrados
    
-  **Cadastrar usuários**
  - Validação de CPF (não permite duplicados)
    
- **Sair do sistema**

---

##  Regras de Negócio

- O valor do depósito deve ser maior que zero
- O saque:
  - Não pode exceder o saldo
  - Não pode ultrapassar o limite por saque
  - Possui um limite máximo de saques
- Cada usuário é identificado por um **CPF único**
- O extrato mostra todas as movimentações realizadas

---

## Como Executar

1. Certifique-se de ter o **Python 3** instalado
2. No terminal, navegue até a pasta do projeto
3. Execute o comando:

```bash
python desafio.py
