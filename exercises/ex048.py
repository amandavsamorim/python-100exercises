soma = 0
for c in range(1, 500+1):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print(f'A soma dos valores ímpares e múltiplos de 3, entre 0 e 500, é igual a {soma}')