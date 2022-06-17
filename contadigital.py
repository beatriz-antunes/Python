# Exercício (5)
# Simule uma tentativa de criar uma conta em uma plataforma digital
# -O programa deve conferir se a conta do usuário que está sendo criado possui no mínimo 12 caracteres e tenha uma senha que possua de no mínimo 8 caracteres e caracteres numéricos 
# -O programa também deve barrar a entrada de caracteres especiais na criação do nome de usuário
# -O programa só deve criar a conta caso todas as condições tenham sido concluídas, se não o programa deve reiniciar voltando para o primeiro processo
# -Quando a conta for criada o programa deve printar a frase: "conta criada!"

import numbers

while True:
    user = input("Usuário -> ")
    if len(user) < 12 or "!" in user or "#" in user:
        print("Seu usuário precisa ter mais de 12 caracteres e não pode ter caracteres especiais.")
        continue
    break


while True:
    senha = input("Senha -> ")
    if len(senha) < 8 and not numbers in senha:
        print("Seu usuário precisa ter mais de 8 caracteres e precisa ter números.")
        continue
    break

print("Conta criada!")