def calculo_E(entrada1, entrada2, elementos, lista):
    saida = []
    l = 2 ** elementos
    if len(entrada1) == 1 and len(entrada2) == 1:
        for c in range(0, l):
            if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
                saida.append(1)
            else:
                saida.append(0)
    elif len(entrada1) > len(entrada2):
        for c in range(0, l):
            if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
                saida.append(1)
            else:
                saida.append(0)
    elif len(entrada2) > len(entrada1):
        for c in range(0, l):
            if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
                saida.append(1)
            else:
                saida.append(0)
    elif len(entrada1) == 2 and len(entrada2) == 2:
        for c in range(0, l):
            if lista[entrada1][c] == 1 and lista[entrada2][c] == 1:
                saida.append(1)
            else:
                saida.append(0)
    return saida