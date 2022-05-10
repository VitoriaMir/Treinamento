# Aumentos múltiplos

salario = float(input('Qual é o salário do funcionário? '))

menor = salario + (salario * 10 / 100) # porcentagem
maior = salario + (salario * 15 / 100)

if salario <= 1250:
    print(f'Com o aumento de 15%, seu salario ficou R${maior}')
else:
    print(f'Com o aumento de 10%, seu salario ficou R${menor}')



