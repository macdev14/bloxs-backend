from apiflask import Schema

class ContaSchema(Schema):
    id_conta = {'type': 'integer'}
    id_pessoa = {'type': 'integer'}
    saldo = {'type': 'number'}
    limite_saque_diario = {'type': 'number'}
    flag_ativo = {'type': 'boolean'}
    tipo_conta = {'type': 'integer'}
    data_criacao = {'type': 'string', 'format': 'date-time'}

class TransacaoSchema(Schema):
    id_transacao = {'type': 'integer'}
    id_conta = {'type': 'integer'}
    valor = {'type': 'number'}
    data_transacao = {'type': 'string', 'format': 'date-time'}

class PessoaSchema(Schema):
    id_pessoa = {'type': 'integer'}
    nome = {'type': 'string'}
    cpf = {'type': 'string', 'pattern': r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'}
    data_nascimento = {'type': 'string', 'format': 'date'}

class UserSchema(Schema):
    username = {'type': 'string'}
    password = {'type': 'string'}