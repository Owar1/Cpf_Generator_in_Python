from random import randint
numeros = str(randint(100000000, 999999999))
novo_cpf = numeros
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

print(f'{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[-2:]}')