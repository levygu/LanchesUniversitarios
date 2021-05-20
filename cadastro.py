from manager_db import *


class Cadastro(object):
    def __init__(self, nome, idade, cpf, email, fone, endereco, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.fone = fone
        self.endereco = endereco
        self.senha = senha

    # INSERE NO BANCO DE DADOS >>>
    def insere(self):
        UsuariosDb.inserir(self.nome, self.idade, self.cpf, self.email, self.fone, self.endereco, self.senha)


print('Preencha os dados: ')
name = input('Nome: ')
age = input('Idade: ')
cpf = input('CPF: ')
email = input('Email: ')
fone = input('Celular: ')
endereco = input('Endereço: ')
senha = input('Senha: ')
Cadastro(name, age, cpf, email, fone, endereco, senha)
Cadastro.insere()

