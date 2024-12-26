distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar sua viagem de {}Km.'.format(distancia))

# Forma simplificada
# preço = distancia * 0.50 if distancia <=200 else distancia * 45

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
