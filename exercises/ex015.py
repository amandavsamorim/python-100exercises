dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados?'))

total = (dias * 60) + (Km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))