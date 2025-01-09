peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))

if IMC < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= IMC < 25:
    print('Você está com o PESO IDEAL')
elif 25 <= IMC < 30:
    print('Você está em SOBREPESO')
elif 30 <= IMC < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA')