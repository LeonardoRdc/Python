import random
import string

print("Bem-vindo ao gerador de senhas!")

def password_generator():
    opcao1 = string.ascii_letters
    opcao2 = string.hexdigits
    opcao3 = string.punctuation
    opcoes = opcao1 + opcao2 + opcao3

    password = ""

    for i in range(0, escolha):
        digito = random.choice(opcoes)
        password = password + digito

    return password


escolha = input("Por favor digite quantos caracteres você deseja em sua senha(MÍNIMO 8 CARACTERES: )")


if escolha.isdigit():
    escolha = int(escolha)
else:
    print("Entrada inválida, por favor use números!")
    quit()

if escolha < 8:
    print("Sua senha deve ter pelo menos 8 caracteres!")
    quit()



generator = password_generator()
print(f"Sua senha foi gerada: {generator}")

