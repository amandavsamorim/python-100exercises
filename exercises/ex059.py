from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int((input('Segundo valor: ')))
opção = 0

while opção != 5:
    print('''    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    opção = int(input('>>>> Qual é sua opção? '))
    if opção == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('O resultado de {} * {} é {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif opção == 4:
        n1 = int(input('Novo primeiro valor: '))
        n2 = int((input('Novo segundo valor: ')))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1.5)
print('Você saiu do programa.')