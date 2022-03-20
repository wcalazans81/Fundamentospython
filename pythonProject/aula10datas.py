from datetime import date, time, datetime, timedelta


def data_hora():
    data_criada = datetime(2022, 10, 13, 11, 31)
    semana = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual)
    print(data_atual.strftime('%c'))
    print(semana[data_atual.weekday()], data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_criada.strftime('%d/%m/%Y %H:%M'))
    # converter str para datetima
    data_arqui = '03/04/2022'
    data_convertida = datetime.strptime(data_arqui, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))
    print(data_convertida.strftime('%d/%m/%Y'))
    nova_data = data_atual - timedelta(days=365)
    print(nova_data)

def data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%y')
    print(data_atual.strftime('%d-%m-%Y'))
    print(type(data_atual))
    print(type(data_atual_str))


def hora():
    horario = time(hour=17, minute=15, second=54)
    horario1 = horario.strftime('%H:%M:%S')
    print(horario)
    print(type(horario))
    print(horario1)
    print(type(horario1))
