while True:
    try:
        prod = float(input('Digite o valor do produto: R$ '))
        break
    except:
        print('por favor digite o valor do produto com números no formato: "R$xxxxx.xx".')

while True:
    est = input('Digite a sigla com duas letras do estado em que ele será vendido:')
    if est.upper() == 'PE':
        prodV = prod + (prod*7/100)           
        print('O preço final do produto é R$',round(prodV, 2))
        break

    elif est.upper() == 'RJ':
        prodV = prod + (prod*15/100)
        print('O preço final do produto é R$',round(prodV, 2))
        break

    elif est.upper() == 'SP':
        prodV = prod + (prod*12/100)         
        print('O preço final do produto é R$',round(prodV, 2))
        break

    elif est.upper() == 'PB':
        prodV = prod + (prod*8/100)
        print('O preço final do produto é R$',round(prodV, 2))
        break

    else:
        print('O estado digitado não é válido, as opções são: (PE, SP, RJ e PB). \n')


