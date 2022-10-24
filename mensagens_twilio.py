from twilio.rest import Client
import re

TWILIO_ACCOUNT_SID = 'AC4609e7c9d2347b823272c7baf0dd13c1'  
AUTH_TOKEN = 'eae9a95e3445581f258d6f37b713e10e' 

# Numero Twilio sandbox
from_whatsapp_number='whatsapp:+14155238886'

def enviar_zap(mensagem, numero):
    try: 
        client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)

        numero = remover_espacos(numero)
        numero = remover_caracteres(numero)
        print('numero formatado: ' + numero)

        message = client.messages.create(body=mensagem,
                        from_=from_whatsapp_number,
                        to=f'whatsapp:+55{numero}')
        if message:
            return 'Mensagem enviada!'
        else: 
            return 'Erro no envio!'
    except:
        print('Erro - Twilio')

def remover_espacos(numero):
    return numero.replace(" ", "")

def remover_caracteres(numero):
    return re.sub(r"[^Z0-9]","", numero)