
# Reajuste Salarial
# Desafio 013
salario = float(input('Qual é o salário: '))
aumento = int(input('Qual é a porcentagem do aumento? '))

salario_nv = salario + (salario * aumento / 100)

print(f'Com um aumento de {aumento}%, este salario passa a ser R${salario_nv:.2f}. ')
