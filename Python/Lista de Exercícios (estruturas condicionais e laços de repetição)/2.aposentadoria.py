while True:
    try:
        idade = int(input('Qual a sua idade?'))
        break
    except:
        print('por favor digite o valor da sua idade com números. Ex:30, 40, 50.')

while True:
    try:
        T_anos = int(input('Quantos anos você trabalhou?'))
        break
    except:
        print('por favor digite o número de anos trabalhados. Ex:5, 15, 30.')

if idade >= 65:
    print('Parabéns, você está apto a se aposentar.')

elif T_anos >= 30:
    print('Parabéns, você está apto a se aposentar.')

elif idade >= 60 and T_anos >= 25:
    print('Parabéns, você está apto a se aposentar.')
else:
    print('Infelizmente você está não apto a se aposentar.')
