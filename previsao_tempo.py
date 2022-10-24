import requests

API_KEY = "0cf2a9a259a44437cfb3555c4fa833e6"
cidade = "Salvador,Br"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&APPID={API_KEY}&lang=pt_br"

def previsao_tempo():
    try:
        print('Previsão do Tempo')
        retorno_request = requests.get(link)        
        retorno_json = retorno_request.json()        
        descricao = retorno_json['weather'][0]['description']
        temperatura = retorno_json['main']['temp'] - 273.15

        previsao = f"O tempo está {descricao} e Temperatura de {temperatura:,.1f} graus Celsius"

        return previsao
    except:
        print('Erro - Previsão do Tempo')
        return 'Erro na Previsão do Tempo' 