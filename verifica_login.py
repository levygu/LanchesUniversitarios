#Verificar o login kapakapakapa

from manager_db import UsuariosDb
if __name__ == '__main__':
	def verificaLogin(login1, senha1):
		def verificaUsername(login = login1):
			#self.senha = senha
			d = UsuariosDb()
			return d.localizar_usuario_por_username(login)
		def verificaSenha (senha = senha1):
			d = UsuariosDb()
			return d.verifica_senha(senha)
		if verificaUsername() == 1:
			print ("Nome de usuário errado")
			return False
		else:
			if verificaSenha() == 1:
				print ("Senha Errada")
				return False
			else:
				return True

	macarao = verificaLogin('levygu','91238912')
	print(macarao)