# Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO


one = float(input('Digite a primeira nota: '))
two = float(input('Digite a segunda nota: '))

media = (one + two) / 2

print(f'Tirando {one} e {two}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('O aluno está REPROVADO')
elif 5.0 <= media <= 6.9:
    print('O aluno está RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')




