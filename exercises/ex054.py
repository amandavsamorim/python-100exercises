from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for c in range(0, 7):
    nasc = int(input('Data de nascimento: '))
    idade = atual - nasc
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print(f'{menores} pessoa(s) ainda não atingiram a maioridade e {maiores} já atingiram.')