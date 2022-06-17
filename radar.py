# Exercício (3)
# Simule um radar de rodovia 
# Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
# -O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa deve indicar que a velocidade não foi fornecida
# -Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o usuário deve mudar de mão
# -Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor dessa multa o excesso de velocidade * 7
# -Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a mecânica acima com o numero sorteado

vMin = 30
vMax = 90

from random import randint as r

vMotorista = input("Velocidade do motorista -> ")

if vMotorista == "":
    vMotorista = r(1, 120)
    print(f"Valor utilizado: {vMotorista}")

else:
    vMotorista = float(vMotorista)    

if vMotorista <= vMin or vMotorista <= 45:
    print("Você está muito lento! Por favor, mude de pista.")

else:
    multa = (vMax - vMotorista) * 7
    print (f"Valor da multa: R$ {multa}.")
