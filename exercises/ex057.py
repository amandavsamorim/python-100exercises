sexo = ''
while sexo != 'M' and sexo != 'F':
        sexo= str(input('Qual o seu sexo? [F/M]: ')).upper()
        if sexo != 'M' and sexo !='F':
                print('Digite um sexo válido')
print('Fim')