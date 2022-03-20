class Erro(Exception):
    pass

class InputErro(Erro):
    def __init__(self, msg):
        self.msg = msg

while True:
    try:
        x = float(input('Digite uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputErro('Não é possível computar um nota maior que 10!')
        if x < 0:
            raise InputErro('Não é possível computar um nota menor que 0!')
        break
    except ValueError:
        print('ERRO! Por favor digite apenas números!!!')
    except InputErro as ex:
        print(ex)
