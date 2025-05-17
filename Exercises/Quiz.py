import random
from PerguntasQuiz import perguntas

print("Bem-vindo ao Quiz de Python")
inicio = input("Deseja começar? (S/N): ").strip().lower()


if inicio in ("sim", "s"):
    print("Começando...\n")
elif inicio in ("nao", "não", "n"):
    print("Saindo da Aplicação...")
else:
    quit()

def perguntas_quiz(texto, resposta_certa, score):
    print(texto)
    resposta = input("Resposta: ").strip().lower()
    if resposta == resposta_certa:
        print("Parabéns, você acertou!")
        score += 1
    else:
        print("Você errou!")
    return score

selecionar_perguntas = random.sample(perguntas, 10)
score = 0

for i in selecionar_perguntas:
    texto = f"{i['pergunta']}\n {i['alternativas']}"
    score = perguntas_quiz(texto, i["resposta"], score)


print(f"Sua pontuação: {score}/10")    