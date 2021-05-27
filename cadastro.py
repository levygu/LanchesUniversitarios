from manager_db import *


class Cadastro(object):
    def __init__(self):
        self.flag = 1
    # INSERE NO BANCO DE DADOS >>>
    def insere(self):
        d = UsuariosDb()
        d.inserir()
        
    def imprime (self):
        d = UsuariosDb()    
        d.imprimir_usuarios()
    


c = Cadastro() 
macarrao = 2

if macarrao == 2:
    c.imprime()

else:
    c.insere()

