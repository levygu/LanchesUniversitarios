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

    def inserir(self, nome1, cpf1, email1, fone1, endereco1, login1, senha1):


        try:
            self.db.cursor.execute("""
            INSERT INTO usuarios1 (nome, cpf, email, fone, endereco, username, senha)
            VALUES (?,?,?,?,?,?,?)
            """, (nome1, cpf1, email1, fone1, endereco1, login1, senha1))
            self.db.commit_db()
            print("Cadastrado com sucesso :)")
        except sqlite3.Error as e:
            print("Error. :(", e)

    def fechar_conexao(self):
        self.db.close_db()

    def ler_todos(self):
        sql = 'SELECT * FROM usuarios1 ORDER BY nome'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_usuarios(self):
        lista = self.ler_todos()
        for c in lista:
            print(c)

    def localizar_usuario_por_username(self, username):
        resultado = self.db.cursor.execute(
            'SELECT username FROM usuarios1 WHERE username = ?', (username,))
        #print (resultado.fetchone())
        self.flag = resultado.fetchone()
        if self.flag == None:
            return 1
        else:
            return 0

    def verifica_senha(self, senha):
        resultado = self.db.cursor.execute(
            'SELECT senha FROM usuarios1 where senha = ?', (senha,))
        self.flag = resultado.fetchone()
        if self.flag == None:
            return 1
        else:
            return 0