# Par ou impar

numero = int(input('Me diga um número qualquer: '))

resul = numero % 2

if resul == 1:
    print(f'O número {numero} é IMPAR')
else: 
    print(f'O número {numero} é PAR')

