from random import choice
import os
import cv2
import string

usuarios = []

def cadastro():
      listuser = open("user.txt","a")
      listsenha = open("senha.txt", "a")

      user = input("Escolha seu ID: ")
      senha = input("Digite a sua senha: ")
      
      #cadastro = ["\n", user,"\n", senha, "\n", "_"*50]
      listuser.write(user+"\n")
      listsenha.write(senha+"\n")

      listuser.close()
      listsenha.close()

def login():
      baseUser = open("user.txt","r")
      baseSenha = open("senha.txt","r")
      listaUser = baseUser.readlines()
      listaSenha = baseSenha.readlines()

      usuario = input("Login: ")
      usuario = usuario+"\n"
      senha = input("Senha:")
      senha = senha+"\n"

      for posicao, compara in enumerate(listaUser):
            if compara==usuario:
                  if listaSenha[posicao]==senha:
                        camera = cv2.VideoCapture(0)
                        car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
                        while True:
                              _, frame = camera.read()
                              gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                              objetos = car_cascade.detectMultiScale(gray, 1.20 , 6)
                              if len(objetos)==0:
                                    print("Erro")
                              else:
                                    for (x, y, w, h) in objetos:
                                          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                                          print("Logado")

                              cv2.imshow("Camera", frame)
                              k = cv2.waitKey(30)
                              if k == 27:
                                    break

                        cv2.destroyAllWindows()
                        camera.release()
      baseUser.close()
      baseSenha.close()

print("Seja Bem Vindo(a) a Autenticação de Três Fatores (ATF)")
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