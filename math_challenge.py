#um cliente solicitou a turma a implementação de um jogo em linguagem Python.
# O jogo consiste em um desafio matemático no qual deve-se responder corretamente as quatro operações básicas.
#Versão dinamica 
import random
from timeit import repeat
a = random.randint(1,5)
b = random.randint(1,5)
respostaInput = input()
resposta = float
soma = a+b
div= a/b
multi = a*b
sub = a-b
acerto = 0
erro = 0


print("Você deve responder corretamente as 8 perguntas de operações básicas: ")

while(respostaInput != resposta):
 while(True):
  print("some os seguintes valores:")
  print(a)
  print(b)
  resposta = soma
  respostaInput = float(input("Insira sua resposta:"))
  if respostaInput == resposta:
    acerto = acerto =+ 1
    break
  else:
   erro = erro =+ 1
   print("Errado.Refaça") 
  repeat
 while(True):
  print("subtraia os seguintes valores:")
  print(a)
  print(b)
  resposta = sub
  respostaInput = float(input("Insira sua resposta:"))
  if respostaInput == resposta:
    acerto = acerto =+ 1
    break
  else:
    erro= erro =+ 1    
    print("Errado.Refaça") 
    repeat
 while(True):
   print("Multiplique os seguintes valores:")
   print(a)
   print(b)
   resposta = multi
   respostaInput = float(input("Insira sua resposta:"))
   if respostaInput == resposta:
     acerto = acerto =+ 1
     break
   else:
    erro = erro =+ 1
    print("Errado.Refaça") 
   repeat
 while(True):
   print("Divida os seguintes valores:")
   print(a)
   print(b)
   resposta = div
   respostaInput = float(input("Insira sua resposta:"))
   if respostaInput == resposta:
     acerto = acerto =+ 1
     break
   else:
     erro = erro =+ 1
     print("Errado.Refaça") 
     repeat
if(acerto > erro):
    print("Parabéns. VocÊ completou o teste com sucesso")
    

