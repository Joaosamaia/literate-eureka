print('*Nesse programa, ao digitar um número inteiro você receberá uma lista de todos os números primos de 1 até o número fornecido.')
lista = [2]
while True:
    try:
        n = int(input('Digite um número:'))
        break
    except:
        print('Digite um número inteiro.')
ip = 0
if n <= 2:
    lista.remove(2)
while ip <= n:
    if ip in lista:
        ip = ip + 1
    elif ip % 2 == 0 and ip not in lista:
        ip = ip + 1
    else:
        lista.append(ip)
        lista.sort()
for i in lista:
    for j in lista:
        if j != i and j != 1 and i != 1:
            if j % i == 0:
                lista.remove(j)
print(lista)