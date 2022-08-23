def porta_e(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
            saida.append(1)
        else:
            saida.append(0)
        print(f"{saida[c]} |", end='')
    print()
    return saida


def porta_ou(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] == 1 or lista[entrada2][c] == 1:
            saida.append(1)
        else:
            saida.append(0)
        print(f"{saida[c]} |", end='')
    print()
    return saida


def porta_en(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
            saida.append(0)
        else:
            saida.append(1)
        print(f"{saida[c]} |", end='')
    print()
    return saida


def porta_oun(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] == 0 and lista[entrada2][c] == 0:
            saida.append(1)
        else:
            saida.append(0)
        print(f"{saida[c]} |", end='')
    print()
    return saida


def porta_exclusiva(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] != lista[entrada2][c]:
            saida.append(1)
        else:
            saida.append(0)
        print(f"{saida[c]} |", end='')
    print()
    return saida


def porta_coincidencia(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    for c in range(0, l):
        if lista[entrada1][c] == lista[entrada2][c]:
            saida.append(1)
        else:
            saida.append(0)
        print(f"{saida[c]} |", end='')
    print()
    return saida
