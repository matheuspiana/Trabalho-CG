from random import choice
import string


usuarios = []




def cadastro():
      listuser = open("user.txt","w")
      listsenha = open("senha.txt", "w")

      user = input("Escolha seu ID: ")
      senha = input("Digite a sua senha: ")
      
      #cadastro = ["\n", user,"\n", senha, "\n", "_"*50]
      listuser.writelines(user)
      listsenha.writelines(senha)

      listuser.close()
      listsenha.close()

def login():
      listuser = open("user.txt","r")
      listuser.read()
      loginid = input("Login: ")
      linhauser = listuser.readlines()
      if linhauser == loginid:
            listuser.close()
            listsenha = open("senha.txt", "r")
            listsenha.read()
            loginsenha = input("Senha: ")
            linhasenha = listsenha.readlines()
            if linhasenha == loginsenha:
                  print("Logado!")
                  listsenha.close()
            else:
                  print("Senha incorreta!")
                  listsenha.close()
      elif linhauser != loginid:
            print("Login não existe")
            listuser.close()


    
    


print("Seja bem a Autenticação de Três Fatores (ATF)")
print("Escolha (1) para Login e (2) para Cadastro.")

escolha = int(input("O que deseja fazer? "))

if escolha == 2:
      cadastro()
elif escolha == 1:
      login()




'''
numeros = int(input("Quantos usuarios deseja adicionar: "))
for x in range(numeros):
    id = input("Escolha seu ID: ")
    usuarios.append(id)


tamanho = 5
valores = string.ascii_lowercase
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)
'''


