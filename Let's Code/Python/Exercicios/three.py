"""Faça um Programa que pergunte o quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato.

O programa deve nos informar:

A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido."""

sl_bruto = float(input('Salario: '))
hr_trab = int(input('Horas: '))
ir = 11 / 100
inss = 8 / 100
sind = 5 / 100

hr = sl_bruto / hr_trab
i = sl_bruto * inss
sin = sl_bruto * sind
sl_liq = sl_bruto - (i + sind)

print(f'A hora trabalhada é R$ {hr_trab} e o valor da hora é R$ {hr:.2f}\n')
print(f'Recebo R$ {sl_bruto} e com os desconto R$ {sl_liq}\n')
print(f'O inss é R$ {i}\n')
print(f' O sindicato é R$ {sin}\n')
