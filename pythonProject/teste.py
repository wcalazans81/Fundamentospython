while True:
    try:
        n = int(input('Digite um número: '))
        print(n)
    except ValueError:
        print('ERRO! Por favor digite um número inteiro válido')

    else:
        break