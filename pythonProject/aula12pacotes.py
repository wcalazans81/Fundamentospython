import requests


def retorna_sados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    #print(response.text)
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep


def retorna_html(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    #retorna_sados_cep(32425695)
    response = retorna_html('https://www.infopedia.pt/dicionarios/lingua-portuguesa/pass%C3%A3o')
    print(response)
