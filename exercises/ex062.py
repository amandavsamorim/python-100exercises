print('Gerador de PA')
print('-=' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

print('Os primeiros 10 termos dessa PA são: ')
termo = a1
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print('{} → '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
