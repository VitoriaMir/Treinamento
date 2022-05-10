nums = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]

def unico(lista):
    for elemento in lista:
        if lista.count(elemento) == 1:  # Aqui vamos retornar o elemento se o conteúdo for 1.
            print(f'O número que não se repete é {elemento}')

unico(nums)
unico(nums2)
unico(nums3)
#
# for elemento in nums:
#     count = nums.count(elemento)
#     if  count == 1: # Aqui vamos retornar o elemento se o conteúdo for 1.
#         print(f'O número que não se repete é {elemento}')
# for elemento1 in nums2:
#     count = nums2.count(elemento1)
#     if count == 1:  # Aqui vamos retornar o elemento se o conteúdo for 1.
#         print(f'O número que não se repete é {elemento1}')
# for elemento2 in nums3:
#     count = nums3.count(elemento2)
#     if count == 1:  # Aqui vamos retornar o elemento se o conteúdo for 1.
#         print(f'O número que não se repete é {elemento2}')
