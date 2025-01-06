n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO valor é maior')
elif n1 < n2:
    print(f'O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')