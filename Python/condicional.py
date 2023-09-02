ent = []
sai = []
temph = 0
tempm = 0

def entrada():
    global ent
    while True:
        ent = input("digite o horário de de entrada: ").split(":")
        ent = [int(x) for x in ent]
        if 0 <= ent[0] <= 23 and 0 <= ent[1] <= 59:
            break
        else:
            print("digite um horário válido. (Ex: 8:41, 12:40, 13:00)")

def saida():
    global sai
    while True:
        sai = input("digite o horário de de saida: ").split(":")
        sai = [int(x) for x in sai]
        if 0 <= sai[0] <= 23 and 0 <= sai[1] <= 59:
            break
        else:
            print("digite um horário válido. (Ex: 8:41, 12:40, 13:00)")

def hour():
    global temph
    if sai[0] > ent[0]:
        temph = sai[0] - ent[0]
    elif sai[0] <= ent[0]:
        enth = 24 - ent[0]
        temph = sai[0] - (-enth)

def min():
    global tempm
    global temph
    if sai[1] >= ent[1]:
        tempm = sai[1] - ent[1]
    else:
        entm = 60 - ent[1]
        tempm = sai[1] + entm
        temph = temph - 1

#optei por usar funções para o caso de querermos fazer o sistema rodar para sempre, ou qualquer outra alteração, 
#ele fica facilmente adaptavel.

entrada()
saida()
hour()
min()

temp = [temph, tempm] #variavel que não está em uso, mas que poderia vir a ter utilidade.

valor = 0.0
x = 0

while x < temph:
    if tempm < 00:
        temph= temph + 1
    if temph >= 1 and x == 0:
        valor = valor + 8
        x = x + 1
    if temph >= 2 and x == 1:
        valor = valor + 8
        x = x + 1
    if temph >= 3 and x == 2:
        valor = valor + 8.5
        x = x + 1
    if temph >= 4 and x == 3:
        valor = valor + 8.5
        x = x + 1
    if temph >= 5 and x >=4:
        valor = valor + 2
        x = x + 1

if valor > 0:
    print ("o valor do estacionamento é de:R$",valor)
elif valor == 0:
    print ("sua estadia não gerou tarifas.")
