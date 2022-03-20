from primo import Mostra_Primo

Mostra_Primo()
while True:
    try:
        num = int(input('Digite um número para ver se este é número primo: '))
    except ValueError:
        print('\033[31mERRO! Por favor digite um número inteiro válido\033[m!')
    else:
        break
temp = []
primo = []
tot = tot1 = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print()
if tot == 2:
    print(f'\033[mO numero {num} foi divisível {tot} vezes e é um número primo...')
else:
    print(f'O numero {num} foi divisível {tot} vezes \033[me por tanto não é um número primo!!!')
i = 1
while i < num+1:
    if num % i == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
    i += 1
print()



