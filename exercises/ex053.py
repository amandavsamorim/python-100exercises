frase = str(input('Sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é igual a {inverso}')
if  inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo.')