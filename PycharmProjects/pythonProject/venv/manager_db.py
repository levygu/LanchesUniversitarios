# CRIAÇÃO E CONEXÃO DE BANCO DE DADOS

import sqlite3


class Connect(object):
    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # Criando a tabela....
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios1 (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    cpf VARCHAR(11) NOT NULL,
                                    email TEXT NOT NULL,
                                    fone TEXT,
                                    endereco TEXT,
                                    username TEXT NOT NULL,
                                    senha TEXT NOT NULL); """)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print('SQLite version: %s' % self.data)
        except sqlite3.Error as e:
            print("Erro ao abrir o banco de dados.", e)

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()


class UsuariosDb(object):
    def __init__(self):
        self.db = Connect('usuarios.db')
        self.tb_name = 'usuarios'

    def inserir(self):
        self.nome = input('Nome: ')
        self.cpf = input ('CPF: ')
        self.email = input('Email: ')
        self.fone = input('Celular: ')
        self. endereco = input('Endereco: ')
        self.login = input('Username: ')
        self.senha = input('Senha: ')

        try:
            self.db.cursor.execute("""
            INSERT INTO usuarios1 (nome, cpf, email, fone, endereco, username, senha)
            VALUES (?,?,?,?,?,?,?)
            """, (self.nome, self.cpf, self.email, self.fone, self.endereco, self.login, self.senha))
            self.db.commit_db()
            print("Cadastrado com sucesso :)")
        except sqlite3.Error as e:
            print("Error. :(", e)

    def fechar_conexao(self):
        self.db.close_db()

    def ler_todos(self):
        sql = 'SELEC * FROM usuarios1 ORDER BY nome'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_usuarios(self):
        lista = self.ler_todos()
        print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
            'id', 'nome', 'cpf', 'email', 'fone', 'endereco', 'username', 'senha'))
        for c in lista:
            print('{:3d} {:23s} {:2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                c[0], c[1], c[2],
                c[3], c[4], c[5],
                c[6], c[7], c[8]))