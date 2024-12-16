produto = float(input('Qual é o valor do produto? R$'))
desconto = (5/100) * produto

print('O produto custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, produto - desconto))