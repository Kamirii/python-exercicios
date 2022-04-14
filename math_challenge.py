#um cliente solicitou a turma a implementação de um jogo em linguagem Python.
# O jogo consiste em um desafio matemático no qual deve-se responder corretamente as quatro operações básicas.
#Versão dinamica 
import random
a = random.randint(1,5)
b = random.randint(1,5)
respostaInput = input()
resposta = int
soma = a+b
div= a/b
multi = a*b
sub = a-b
cont = 0
erro = 0

print("Você deve responder corretamente as 8 perguntas de operações básicas: ")
print("some os seguintes valores:")
print(a)
print(b)
resposta = soma
respostaInput = int(input("Insira sua resposta:"))
if respostaInput == resposta:
    cont = cont + 1
else:
  erro = erro + 1
print("subtraia os seguintes valores:")
print(a)
print(b)
resposta = sub
respostaInput = int(input("Insira sua resposta:"))
if respostaInput == resposta:
    cont = cont + 1
else:
    erro= erro +1    
print("multiplique os seguintes valores:")
print(a)
print(b)
resposta = multi
respostaInput = int(input("Insira sua resposta:"))
if respostaInput == resposta:
    cont = cont + 1
else:
    erro= erro +1
print("Divida os seguintes valores:")
print(a)
print(b)
resposta = div
respostaInput = int(input("Insira sua resposta:"))
if respostaInput == resposta:
    cont = cont + 1
else:
    erro= erro +1
print(cont , "acertos")
print(erro , "erros")
