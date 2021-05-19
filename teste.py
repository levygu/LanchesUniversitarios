class Usuario:
    def __init__(self, nome, email, numero, endereco, senha):
        self.nome = nome
        self.email = email
        self.numero = numero
        self.endereco = endereco
        self.senha = senha
    
class Funcionario(Usuario):
    def __init__(self, nome, email, numero, endereco, senha, key, tipo):
        super().__init__(nome, email, numero, endereco, senha)
        self.key = key
        self.tipo = tipo

class Cliente(Usuario):
    
    def __init__(self, nome, email, numero, endereco, senha):
        super().__init__(nome, email, numero, endereco, senha)
        
    def mostraPerfil(self):
        return self.nome, self.email, self.numero, self.endereco
    
    def editaPerfil(self, nome, email, numero, endereco, senha):
        
        self.nome = nome
        self.email = email
        self.numero = numero
        self.endereco = endereco
        self.senha = senha
    
class Administrador(Usuario):
    
    def __init__(self, nome, email, numero, endereco, senha):
        super().__init__(nome, email, numero, endereco, senha)

#Teste

print('################################')
print('Olá Seja Bem Vindo ^_^')
print('1 - Primeiro Acesso')
print('2 - Login')
print('################################')
menu = int(input('Digite o número correspondente: '))
if menu == 1:
    print ('###############################')
    print ('Você deseja se cadastrar como: ')
    print ('1 - Administrador')
    print ('2 - Funcionario')
    print ('3 - Cliente')
    print ('################################')
    menu2 = int(input('Digite o número correspondente: '))
    
    if menu2 == 1:
        
        nome1 = input ('Digite seu nome: ')
        email1 = input ('Digite seu email: ')
        numero1= input ('Digite seu número: ')
        endereco1 = input ('Digite seu endereço: ')
        senha1 = input ('Digite sua senha: ')
        adm1 = Administrador(nome1, email1, numero1, endereco1, senha1)
        print('Cadastro efetuado com sucesso. ^_^')
        
    if menu2 == 2:
        
        nome = input ('Digite seu nome: ')
        email = input ('Digite seu email: ')
        numero = input ('Digite seu número: ')
        endereco = input ('Digite seu endereço: ')
        senha = input ('Digite sua senha: ')
        key = input ('Digite a Key: ')
        tipo = input ('Digite o tipo: ')
        funcionario1= Funcionario(nome, email, numero, endereco, senha)
        print('Cadastro efetuado com sucesso. ^_^')  
        
    if menu2 == 3:
        
        nome = input ('Digite seu nome: ')
        email = input ('Digite seu email: ')
        numero = input ('Digite seu número: ')
        endereco = input ('Digite seu endereço: ')
        senha = input ('Digite sua senha: ')
        cliente1 =  Cliente(nome, email, numero, endereco, senha)
        print('Cadastro efetuado com sucesso. ^_^')
        
if menu==2:
    print ('Essa funcionalidade ainda não está pronta :(((')
