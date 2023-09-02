sim = 0
nao = 0

nome = input("Digite o nome do investigado: ")

perguntas = [
        "Telefonou para a vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Devia para a vítima? ",
        "Já trabalhou com a vítima? "
    ]

def perguntar(pergunta):
    while True:
        resposta = input(pergunta).upper()
        if resposta == "SIM":
            return True
        elif resposta == "NAO" or resposta == "NÃO":
            return False
        else:
            print("Resposta inválida. Por favor, insira 'sim' ou 'não'.")

for pergunta in perguntas:
    if perguntar(pergunta):
        sim += 1
    else:
        nao += 1

if sim < 2 and nao <= 5:
    print(nome, "é inocente")

if sim == 2:
    print(nome, "é um(a) supeito")

if sim == 3 or sim == 4:
    print(nome, "é um(a) cúmplice")

if sim == 5:
    print(nome, "é o(a) assassino")



     





