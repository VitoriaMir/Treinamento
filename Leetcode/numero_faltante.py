# Dado um array de inteiros contendo N numeros distintos de 0 a N,
# retorne o único numero que está faltando no array entre 0 e N
# Exemplos:
# Input: nums = [3,0,1]
# Output: 2
# Input: nums = [0,1]
# Output: 2
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8



from ast import Slice


nums = [3,0,1]
nums1 = [9,6,4,2,3,5,7,0,1]
nums2 = [0,1]

# já  que existem 3 números
# n = 3
# for falta in range(0,n):
def encontra_faltando(num):
    for falta in range(0,len(num)): # Trazer o que esta no intervalo de 0 a N
        if falta not in num:
            print(falta)

encontra_faltando(nums)
encontra_faltando(nums1)
encontra_faltando(nums2)