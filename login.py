from PyQt5 import  uic,QtWidgets
import sqlite3

def chama_segunda_tela():
    verificalogin= True
    primeira_tela.label_12.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "wanya123" and senha == "123456":
        primeira_tela.close()
        segunda_tela.show()
    else :
        primeira_tela.label_12.setText("Dados de login incorretos!")
    

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    senha= tela_cadastro.lineEdit_4.text()
    n_senha= tela_cadastro.lineEdit_5.text()

    if (senha == n_senha ):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro(nome text, celular text, email text, senha text, n_senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+senha+"','"+n_senha+"')")

            banco.commit()
            banco.close()
            tela_cadastro.label_2.setText("USUÁRUI CADASTRADO COM SUCESSO")
        except sqlite3.Error as erro:
            print ("Erro ao inserir os dados:", erro)
    else:
        tela_cadastro.label_2.setText("AS SENHAS ESTÃO DIFERENTES")


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
 
primeira_tela.show()
app.exec()