num = int(input('Digite um número: '))

for c in range(2, 5):
    calc = num % c == 0
if calc == 1:
    print(f'O número {num} não é primo')
else:
    print(f'O número {num} é primo')