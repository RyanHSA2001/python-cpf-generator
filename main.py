import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

i = 10

repeat = 0
while repeat != 2:
    repeat += 1

    soma = 0
    for digito in cpf:
        operation = int(digito) * i

        soma += operation

        i -= 1

    product = (soma * 10) % 11

    digit = 0 if product > 9 else product

    cpf += str(digit)

    i = 11

cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

print(cpf)
