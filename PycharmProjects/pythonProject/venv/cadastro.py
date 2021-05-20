from manager_db import *


class Cadastro(object):
    def __init__(self):
        self.flag = 1
    # INSERE NO BANCO DE DADOS >>>
    def insere(self):
        d = UsuariosDb()
        d.inserir()
        d.imprimir_usuarios()

c = Cadastro()
c.insere()

