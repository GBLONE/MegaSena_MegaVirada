import random

# Resultados da Mega da Virada
mega_da_virada = [
    [4, 5, 10, 34, 58, 59],
    [12, 15, 23, 32, 33, 46],
    [17, 20, 22, 35, 41, 42],
    [3, 35, 38, 40, 57, 58],
    [5, 10, 12, 18, 25, 33],
    [3, 6, 10, 17, 34, 37],
    [5, 11, 22, 24, 51, 53],
    [2, 18, 31, 42, 51, 56],
    [1, 5, 11, 16, 20, 56],
    [20, 30, 36, 38, 47, 53],
    [14, 32, 33, 36, 41, 52],
    [3, 4, 29, 36, 45, 55],
    [2, 10, 34, 37, 43, 50],
    [10, 27, 40, 46, 49, 58],
    [1, 11, 26, 51, 59, 60],
    [7, 17, 19, 34, 36, 39],
    [10, 14, 32, 47, 50, 56],
    [3, 9, 35, 37, 41, 49]
]

# Resultados da Mega Sena
mega_sena = [
    [17, 20, 27, 28, 31, 37],
    [1, 5, 6, 37, 44, 53],
    [4, 5, 30, 33, 41, 52],
    [7, 16, 21, 33, 55, 60],
    [1, 5, 14, 23, 35, 45],
    [2, 4, 21, 22, 30, 48],
    [1, 2, 14, 37, 47, 50],
    [6, 7, 29, 39, 41, 55],
    [1, 8, 11, 22, 30, 35],
    [14, 16, 34, 35, 49, 56],
    [1, 8, 13, 25, 28, 31],
    [2, 5, 10, 29, 34, 41],
    [1, 6, 28, 37, 44, 56],
    [2, 3, 6, 18, 20, 28],
    [1, 4, 5, 14, 45, 56],
    [6, 7, 10, 27, 28, 46],
    [1, 2, 23, 26, 47, 58],
    [2, 4, 23, 38, 46, 56],
    [1, 5, 23, 25, 28, 31],
    [2, 4, 21, 23, 29, 56],
]

# Gerar números aleatórios para a Mega da Virada
numeros_mega_da_virada = []
while len(numeros_mega_da_virada) < 6:
    numero = random.randint(1, 60)
    if numero not in numeros_mega_da_virada:
        numeros_mega_da_virada.append(numero)

# Gerar números aleatórios para a Mega Sena
numeros_mega_sena = []
while len(numeros_mega_sena) < 6:
    numero = random.randint(1, 60)
    if numero not in numeros_mega_sena:
        numeros_mega_sena.append(numero)

# Salvando o resultado da Mega Sena
with open('ResulMegaSena.txt', 'a') as arquivo:
    numberSena = str(numeros_mega_sena)
    arquivo.write(numberSena.strip('[]') + '\n')
    arquivo.close()

# Salvando o resultado da Mega da Virada
with open('ResulMegaVirada.txt', 'a') as arquivo:
    numberVirada = str(numeros_mega_da_virada)
    arquivo.write(numberVirada.strip('[]') + '\n')
    arquivo.close()

# Verificar se os números já foram sorteados antes
if numeros_mega_da_virada in mega_da_virada:
    print("Os números da Mega da Virada já foram sorteados antes!")
    print(f'Número da Mega da Virada são: {numeros_mega_da_virada}')
else:
    print("Os números da Mega da Virada ainda não foram sorteados.")
    print(f'Número da Mega da Virada são: {numeros_mega_da_virada}')

if numeros_mega_sena in mega_sena:
    print("Os números da Mega Sena já foram sorteados antes!")
    print(f'Números da Mega Sena são: {numeros_mega_sena}')
else:
    print("Os números da Mega Sena ainda não foram sorteados.")
    print(f'Números da Mega Sena são: {numeros_mega_sena}')


