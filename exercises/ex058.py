import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

computador = random.randint(0, 10)
jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

tentativa = 1
while jogador != computador:
    print(f'GANHEI! Eu pensei em outro número e não no {jogador}')
    jogador = int(input('Tente novamente: '))
    tentativa += 1
print('PARABÉNS! Você conseguiu me vencer')
print('Você precisou de {} tentativas para ganhar de mim'.format(tentativa))
