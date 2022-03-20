n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 == n2:
    print(f'Os valores {n1} e {n2} são iquais.')
elif n1 > n2:
    print(f'Os valores {n1} e {n2}  {n1} é maior.')
elif n1 < n2:
    print(f'Os valores {n1} e {n2} {n2} é maior.')
if n2 % 2 == 0:
    print(f'O valor {n2} é par')
if n1 % 2 == 0:
    print(f'O valor {n1} é par')
