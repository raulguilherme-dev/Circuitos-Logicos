import portas
from copy import deepcopy
from time import sleep

print(f"[{' -' * 5}TABELA VERDADE{' - ' * 5}]\n")

#Define os elementos básicos da tabela verdade à ser montada.
#Quantidade de elementos de entrada e linhas da tabela.
elementos = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[]}
while True:
    entry = str(input("Quantos elementos de entrada sua expressão possui? "))
    if entry.isnumeric():
        entry = int(entry)
        break
    else:
        print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
linhas = 2 ** entry
entradas = {}
cont = 0
for k, v in elementos.items():
    if cont >= entry:
        break
    entradas[k] = v
    cont +=1

#Cria uma lista com as keys do dicionário para iterar um dicionário a partir do final.
keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
dic = {}
for c in range(1, len(entradas)+1):
    dic[c] = keys[c-1]
ind = list(dic.keys())
ind = reversed(ind)

#Adiciona os elementos (0 ou 1) da tabela verdade.
salto = 2
for i in ind:
    contador = 1
    for c in range(0, linhas):
        if contador <= salto / 2:
            entradas[dic[i]].append(0)
        elif contador > salto / 2:
            entradas[dic[i]].append(1)

        if contador == salto:
            contador = 1
        else:
            contador +=1
    salto = salto * 2

#Apresenta a tabela verdade na tela
print()
print("Tabela verdade dos elementos de entrada: \n")
for k, v in entradas.items():
    print(f"{k}: |", end="")
    for c in range(0, len(v)):
        print(f"{v[c]} |", end="")
    print()
sleep(1)

#cria uma tabela verdade com os valores de entrada NEGADOS e os apresenta na tela.
n_entradas = deepcopy(entradas)

for c in range(len(n_entradas.keys())):
    n_entradas[keys[c]+'!'] = n_entradas[keys[c]]
    del n_entradas[keys[c]]

print()
print("Tabela verdade dos elementos de entrada NEGADOS: \n")
for k, v in n_entradas.items():
    entradas[k] = v
    print(f"{k}: |", end="")
    for c in range(0, len(v)):
        if v[c] == 0:
            v[c] = 1
        elif v[c] == 1:
            v[c] = 0
        print(f"{v[c]} |", end="")
    print()
sleep(1)

print()

#Cria um dicionário que relaciona as opções de portas ao caracter que o representa (Dentro do programa).
dic_chaves = {1:".", 2:"+", 3:";", 4:"#", 5:"@", 6:"&"}

#Menu de portas para a escolha do usuário.
while True:
    print(f"""\nQual tipo de operação você deseja fazer?
    {'[ 1 ] E':<18}{'[ 2 ] OU':<18}{'[ 3 ] NÃO E':<18}
    {'[ 4 ] NÃO OU':<18}{'[ 5 ] EXCLUSIVA':<18}{'[ 6 ] COINCIDÊNCIA':<18}
    {'[ 7 ] VER TABELA':<18}
    {'[ 0 ] SAIR DO PROGRAMA':>40}""")

    while True:
        while True:
            user = str(input("Sua escolha: "))
            if user.isnumeric():
                user = int(user)
                break
            else:
                print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
        if 0 <= user <= 7:
            break
        else:
            print("POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA! ", end='')

    #Usuário informa quais entradas a porta escolhida recebe.
    if 1 <= user <= 6:
        print("\nIndique os elementos de entrada que irá usar: ")
        print("Caso precise utilizar uma entrada negada, apenas coloque uma '!' "
              "exclamação após o nome da porta. exemplo (A!)")
        while True:
            ent1 = str(input("Entrada 1: ")).strip().upper()
            if ent1 not in entradas.keys():
                print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
            else:
                break

        while True:
            ent2 = str(input("Entrada 2: ")).strip().upper()
            if ent2 not in entradas.keys():
                print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
            else:
                break
        chave = "(" + ent1 + dic_chaves[user] + ent2 + ")"
        print()
        print(f"{chave}: ", end="")

    #Aciona uma função baseado nas escolhas do usuário
    if user == 0:
        break

    elif user == 1:
        entradas[chave] = portas.porta_e(ent1, ent2, entry, entradas)

    elif user == 2:
        entradas[chave] = portas.porta_ou(ent1, ent2, entry, entradas)

    elif user == 3:
        entradas[chave] = portas.porta_en(ent1, ent2, entry, entradas)

    elif user == 4:
        entradas[chave] = portas.porta_oun(ent1, ent2, entry, entradas)

    elif user == 5:
        entradas[chave] = portas.porta_exclusiva(ent1, ent2, entry, entradas)

    elif user == 6:
        entradas[chave] = portas.porta_coincidencia(ent1, ent2, entry, entradas)

    elif user == 7:
        print()
        print("Tabela verdade: \n")
        for k, v in entradas.items():
            print(f"{k}: |", end="")
            for c in range(0, len(v)):
                print(f"{v[c]} |", end="")
            print()
        sleep(5)
        print()
