from random import choice
import string


usuarios = []
arquivo = open("ids.txt","a")



def cadastro():
      user = input("Escolha seu ID: ")
      senha = input("Digite a sua senha: ")
      
      cadastro = ["\n", user,"\n", senha, "\n", "_"*50]
      arquivo.writelines(cadastro)

def login():
    arquivo.read()
    print (arquivo)


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


