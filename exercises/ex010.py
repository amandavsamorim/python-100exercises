# conversor de moedas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 6

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))