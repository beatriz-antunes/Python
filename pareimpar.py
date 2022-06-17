# Exercício (7)
# Crie um script que receba 6 números e retorne quais são os números pares e quais são os ímpares

num1 = int(input("Digite o Num1 -> "))
num2 = int(input("Digite o Num2 -> "))
num3 = int(input("Digite o Num3 -> "))
num4 = int(input("Digite o Num4 -> "))
num5 = int(input("Digite o Num5 -> "))
num6 = int(input("Digite o Num6 -> "))

numeros = [num1, num2, num3, num4, num5, num6]

i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        print(f"O número {numeros[i]} é par.")
    else:
        print(f"O número {numeros[i]} é ímpar.")
    i += 1