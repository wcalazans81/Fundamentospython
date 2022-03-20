def criar_arquivo(testo):
    arquivo = open('pasta.txt', 'w')
    arquivo.write(testo)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('pasta.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
'''
PARA GERAR ARQUIVOS EM QUALQUER LUGAR DO SEU COMPUTADOR E SÓ INDICAR O CAMINHO
'''