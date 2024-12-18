nome = str(input('Digite seu nome completo: ')).strip()

maiusculo = nome.upper()
minusculo = nome.lower()
separa = nome.split()

print('Seu nome em maiúsculas é {}'.format(maiusculo))
print('Seu nome em minúsculas é {}'.format(minusculo))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))