def Tete_div(a, b):
    if b == 1:
        return 0
    elif a % b == 0:
        return 1
    else:
        return Tete_div(a, b-1)


def Teste_Primo(n):
    if Tete_div(n, n-1) == 0:
        return 1
    else:
        return 0


def Gerar_Primo(n, k, m, vetor ):
    if Teste_Primo(m) == 1:
        vetor.append(m)
        k += 1
    if n == k:
        return
    else:
        Gerar_Primo(n, k, m+1, vetor)


def Mostra_Primo():
    while True:
        try:
            n = int(input('Quantos números primos Você quer gerar?  '))
        except ValueError:
            print('\033[31mERRO! Por favor digite um número inteiro válido\033[m!')
        else:
            break
    v = []
    Gerar_Primo(n, 0, 2, v)
    for i in v:
        print(i, end=' ')
    print()


