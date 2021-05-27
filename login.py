from PyQt5 import  uic,QtWidgets
from verifica_login import verificaLogin

def chama_segunda_tela():
    primeira_tela.label_12.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    resultado = verificaLogin(nome_usuario,senha)
    if resultado == 1:
        #Aqui faz mostrar uma tela para nome de usuario errado
    
    if resultado == 2:
        #aqui faz mostrar uma tela para senha errada

    if resultado ==3:
        #deu tudo certo, a pessoa logou 


def logout():
    segunda_tela.close()
    primeira_tela.show()

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

 
primeira_tela.show()
app.exec()