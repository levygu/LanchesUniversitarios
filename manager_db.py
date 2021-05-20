# CRIAÇÃO E CONEXÃO DE BANCO DE DADOS

import sqlite3


class Connect(object):
    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # Criando a tabela....
            self.cursor.execute("""CREATE TABLE usuarios (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    idade INTEGER,
                                    cpf VARCHAR(11) NOT NULL,
                                    email TEXT NOT NULL,
                                    fone TEXT,
                                    endereco TEXT,
                                    senha TEXT); """)
            self.data = self.cursor.fetchone()
            print('SQLite version: %s' % self.data)
        except sqlite3.Error:
            print("Erro ao abrir o banco de dados.")
            return False

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

    def inserir(self, nome, idade, cpf, email, fone, endereco, senha):
        self.db.cursor.execute("""
        INSERT INTO usuarios (nome, idade, cpf, email, fone, endereco, senha)
        VALUES (?,?,?,?,?,?,?)
        """, (nome, idade, cpf, email, fone, endereco, senha))
        self.db.commit_db()
        print("Cadastrado com sucesso :)")

    def fechar_conexao(self):
        self.db.close_db()
