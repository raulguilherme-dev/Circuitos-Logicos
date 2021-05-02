from copy import deepcopy

#Caracteres que serão usados no código

neg = '!' #NEGAÇÃO
e = '.' #E
negE = '¬.' #NÃO E
ou = '+' #OU
negOu = '¬+' #NÃO OU
exc = '@' #EXCLUSIVA
coinc = '&' #COINCIDÊNCIA

print(f"[{' -' * 5}TABELA VERDADE{' - ' * 5}]\n")

#Define os elementos básicos da tabela verdade à ser montada.
#Quantidade de elementos de entrada e linhas da tabela.
elementos = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[]}
entry = int(input("Quantos elementos de entrada sua expressão possui? "))
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

#Cria uma versão oposta a da tabela verdade criada. Ou seja,
#cria uma tabela verdade com os valores de entrada NEGADOS e os apresenta na tela.
n_entradas = deepcopy(entradas)
print()
print("Tabela verdade dos elementos de entrada NEGADOS: ")
for k, v in n_entradas.items():
    print(f"{k}: |", end="")
    for c in range(0, len(v)):
        if v[c] == 0:
            v[c] = 1
        elif v[c] == 1:
            v[c] = 0
        print(f"{v[c]} |", end="")
    print()

print()
resultados = {}
while True:
    print(f"""Qual tipo de operação você deseja fazer?
    {'[ 1 ] E':<18}{'[ 2 ] OU':<18}{'[ 3 ] NÃO E':<18}
    {'[ 4 ] NÃO OU':<18}{'[ 5 ] EXCLUSIVA':<18}{'[ 6 ] COINCIDÊNCIA':<18}""")
    while True:
        user = int(input("Sua escolha: "))
        if 0 < user <= 6:
            break
        else:
            print("POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA! ", end='')
    print("Indique os elementos de entrada que irá usar: ")
    print("Caso precise utilizar uma entrada negada, apenas coloque uma '!' "
          "exclamação após o nome da porta. exemplo (A!)")
    while True:
        ent1 = str(input("Entrada 1: ")).strip().upper()[:2]
        if ent1[0] not in entradas.keys() or len(ent1) > 1 and ent1[1] != '!':
            print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
        else:
            break

    while True:
        ent2 = str(input("Entrada 2: ")).strip().upper()[:2]
        if ent2[0] not in entradas.keys() or len(ent2) > 1 and ent2[1] != '!':
            print("POR FAVOR ESCOLHA UM VALOR VÁLIDO! ", end='')
        else:
            break

    if user == 1:
        resultados[ent1 + e + ent2] = []
        if len(ent1) == 1 and len(ent2) == 1:
            for c in range(0, linhas):
                if entradas[ent1[0]][c] == 1 and entradas[ent2[0]][c] == 1:
                    resultados[ent1+e+ent2].append(1)
                else:
                    resultados[ent1+e+ent2].append(0)
        elif len(ent1) > len(ent2):
            for c in range(0, linhas):
                if n_entradas[ent1[0]][c] == 1 and entradas[ent2[0]][c] == 1:
                    resultados[ent1+e+ent2].append(1)
                else:
                    resultados[ent1+e+ent2].append(0)
        elif len(ent2) > len(ent1):
            for c in range(0, linhas):
                if entradas[ent1[0]][c] == 1 and n_entradas[ent2[0]][c] == 1:
                    resultados[ent1 + e + ent2].append(1)
                else:
                    resultados[ent1 + e + ent2].append(0)
        elif len(ent1) == 2 and len(ent2) == 2:
            for c in range(0, linhas):
                if n_entradas[ent1[0]][c] == 1 and n_entradas[ent2[0]][c] == 1:
                    resultados[ent1+e+ent2].append(1)
                else:
                    resultados[ent1+e+ent2].append(0)
        print(resultados)

    if user == 2:
        resultados[ent1 + ou + ent2] = []
        if len(ent1) == 1 and len(ent2) == 1:
            for c in range(0, linhas):
                if entradas[ent1[0]][c] == 1 or entradas[ent2[0]][c] == 1:
                    resultados[ent1 + ou + ent2].append(1)
                else:
                    resultados[ent1 + ou + ent2].append(0)
        elif len(ent1) > len(ent2):
            for c in range(0, linhas):
                if n_entradas[ent1[0]][c] == 1 or entradas[ent2[0]][c] == 1:
                    resultados[ent1 + ou + ent2].append(1)
                else:
                    resultados[ent1 + ou + ent2].append(0)
        elif len(ent2) > len(ent1):
            for c in range(0, linhas):
                if entradas[ent1[0]][c] == 1 or n_entradas[ent2[0]][c] == 1:
                    resultados[ent1 + ou + ent2].append(1)
                else:
                    resultados[ent1 + ou + ent2].append(0)
        elif len(ent1) == 2 and len(ent2) == 2:
            for c in range(0, linhas):
                if n_entradas[ent1[0]][c] == 1 or n_entradas[ent2[0]][c] == 1:
                    resultados[ent1 + ou + ent2].append(1)
                else:
                    resultados[ent1 + ou + ent2].append(0)
        print(resultados)