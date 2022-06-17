# Exercício (6)
# Use a estrutura de loop for para que o programa retorne todos números pares 
# de 0 até um número especificado por terminal

num = int(input("Digite um número -> "))

for numero in range(0, num):
    if numero % 2 == 0:
        print(numero)