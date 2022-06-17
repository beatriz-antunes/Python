# Exercício (1)
# Crie um programa que peça ao usuário um número, 
# e retorne todos os múltiplos do número escolhido pelo usuário de 1 a 10


numero = int(input("Escolha um número de 1 a 10 -> "))

for multiplo in range(1, 11):
    if multiplo % numero == 0:
        print(multiplo)
