while True:
    try:
        num = int(input('Digite o número do mês:'))
        if num <= 12 and num != 0:
            break
        else:
            print('por favor digite um número entre 1 e 12.')
    except:
        print('por favor digite um número inteiro entre 1 e 12.')

if num == 1:
    print('O número digitado corresponde ao mês de Janeiro.')

if num == 2:
    print('O número digitado corresponde ao mês de Fevereiro.')

if num == 3:
    print('O número digitado corresponde ao mês de Março.')

if num == 4:
    print('O número digitado corresponde ao mês de Abril.')

if num == 5:
    print('O número digitado corresponde ao mês de Maio.')

if num == 6:
    print('O número digitado corresponde ao mês de Junho.')

if num == 7:
    print('O número digitado corresponde ao mês de Julho.')

if num == 8:
    print('O número digitado corresponde ao mês de Agosto.')

if num == 9:
    print('O número digitado corresponde ao mês de Setembro.')

if num == 10:
    print('O número digitado corresponde ao mês de outubro.')

if num == 11:
    print('O número digitado corresponde ao mês de Novembro.')

if num == 12:
    print('O número digitado corresponde ao mês de Dezembro.')