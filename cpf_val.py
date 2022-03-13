while True:
    cpf = input('Digite um cpf: ')
    novo_cpf = cpf[:-2]
    regressivo = 10
    total = 0

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * regressivo

        regressivo -= 1
        if regressivo < 2:
            regressivo = 11

            d = 11 - (total % 11)

            if d > 9:
                d = 0

            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if novo_cpf == cpf and not sequencia:
        print('Cpf valido')
    else:
        print('Cpf invalido')
