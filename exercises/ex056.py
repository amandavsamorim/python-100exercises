somaidade = 0
maioridadehomem = 0
nomevelho = 0
mulher = 0
for p in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F ou M): ')).strip()
    print('-'*20)

    #média
    somaidade += idade

    #nome do mais velho
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    #mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulher += 1

print('A média de idade do grupo é de {}'.format(somaidade / 4))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos.'.format(mulher))
