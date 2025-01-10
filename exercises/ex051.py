a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

print('Os primeiros 10 termos dessa PA são: ')
for c in range(1, 10+1):
    an = a1 + (c - 1) * r
    print(an, end=' → ')
print('Acabou')