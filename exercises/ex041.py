from datetime import date
nasc = int(input('Ano de Nascimento: '))

atual = date.today().year
idade = atual - nasc

print('Quem nasceu em {} tem {} anos.'.format(nasc,idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
else:
    print('Digite um ano válido')