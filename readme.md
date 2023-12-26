# Nome do Projeto

Desafio Técnico - Bloxs

## Visão Geral

API que realize operações bancárias básicas.

## Requisitos

- Python 3.8.16
- MySQL

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/macdev14/bloxs.git
    cd bloxs
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Crie um arquivo .env com as credenciais de conexão ao banco de dados:**

    ```bash
    USER = 'root'
    PASSWORD = 'root'
    HOST = '127.0.0.1'
    PORT = '8889' 
    DATABASE = 'bloxs'
    ```
4. **Aplique as migrations criando as tabelas**
    ```bash
    flask db upgrade
    ```
5. **Inicie a API**
    ```bash
    flask run
    ```
# Documentação da API

## Contas Bancárias

### Criação de uma conta bancária:
- **Endpoint:** `POST /api/accounts`
- **Descrição:** Cria uma nova conta bancária.
- **Payload:** Dados necessários para criar a conta (ex: id_pessoa, tipo_conta).
- **Retorno:** Retorna os detalhes da conta recém-criada.

### Consulta de saldo de uma conta:
- **Endpoint:** `GET /api/accounts/{id_conta}`
- **Descrição:** Retorna o saldo atual de uma conta específica.
- **Retorno:** Retorna o saldo da conta.

### Depósito em uma conta:
- **Endpoint:** `POST /api/accounts/{id_conta}/deposit`
- **Descrição:** Realiza um depósito em uma conta específica.
- **Payload:** Valor a ser depositado na conta.
- **Retorno:** Retorna os detalhes da transação de depósito.

### Saque em uma conta:
- **Endpoint:** `POST /api/accounts/{id_conta}/withdraw`
- **Descrição:** Realiza um saque em uma conta específica.
- **Payload:** Valor a ser retirado da conta.
- **Retorno:** Retorna os detalhes da transação de saque.

### Bloqueio de uma conta:
- **Endpoint:** `PUT /api/accounts/{id_conta}/block`
- **Descrição:** Bloqueia uma conta específica.
- **Retorno:** Retorna confirmação do bloqueio.

### Recuperação do extrato de transações de uma conta:
- **Endpoint:** `GET /api/accounts/{id_conta}/transactions`
- **Descrição:** Retorna o extrato de transações de uma conta específica.
- **Retorno:** Retorna uma lista de transações relacionadas à conta.

## Transações

### Criação de uma transação:
- **Endpoint:** `POST /api/transactions`
- **Descrição:** Cria uma nova transação.
- **Payload:** Dados necessários para criar a transação (ex: id_conta, valor).
- **Retorno:** Retorna os detalhes da transação criada.

### Atualização de uma transação:
- **Endpoint:** `PUT /api/transactions/{id_transacao}`
- **Descrição:** Atualiza os detalhes de uma transação específica.
- **Payload:** Novos dados para a transação.
- **Retorno:** Retorna os detalhes da transação atualizada.

### Exclusão de uma transação:
- **Endpoint:** `DELETE /api/transactions/{id_transacao}`
- **Descrição:** Remove uma transação específica.
- **Retorno:** Retorna confirmação da remoção.

## Pessoas (Clientes)

### Consulta de informações de uma pessoa:
- **Endpoint:** `GET /api/people/{id_pessoa}`
- **Descrição:** Retorna informações de uma pessoa específica.
- **Retorno:** Retorna os detalhes da pessoa.
