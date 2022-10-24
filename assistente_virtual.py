from asyncio.windows_events import NULL
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from io import BytesIO
from datetime import datetime
from pygame import mixer
import asyncio
import wikipedia_resumo as wikipedia
import previsao_tempo as tempo
import mensagens_twilio as mensagens

#Função para ouvir e reconhecer a fala, retornando um texto
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)        
                
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        print("Reconhecendo audio...")
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

#Converter o texto para audio e tocar o audio 
async def gerar_audio(texto):
    
    try:        
        mp3_fp = BytesIO()
        tts = gTTS(texto,lang='pt-br')

        tts.write_to_fp(mp3_fp)

        mixer.init()
        mixer.music.load(mp3_fp, 'mp3')
        mixer.music.play()

        while mixer.music.get_busy():
            continue

        #await asyncio.sleep(2) 
    except:
        print('Erro - Gerar Audio') 

def executar_comando(texto):
    COMANDOS_WIKIPEDIA = ['wikipedia', 'wikipédia', 'pesquisar', 'buscar']
    COMANDOS_TEMPO = ['previsão', 'previsao', 'tempo']
    COMANDOS_MENSAGENS = ['mensagem', 'zap', 'whatsapp']
    
    if bool([comando for comando in COMANDOS_WIKIPEDIA if(comando in texto.lower())]):
        return wikipedia.resumo(texto)
    elif bool([comando for comando in COMANDOS_TEMPO if(comando in texto.lower())]):
        return tempo.previsao_tempo()
    elif "navegador" in texto.lower():
        os.system("start Chrome.exe")
    elif "excel" in texto.lower():
        os.system("start Excel.exe")
    elif bool([comando for comando in COMANDOS_MENSAGENS if(comando in texto.lower())]):
        try:
            asyncio.run(gerar_audio('Diga qual a mensagem:'))

            mensagem = ouvir_microfone()
            print('mensagem: ' + mensagem)

            asyncio.run(gerar_audio('Diga qual o numero do whatsapp com o DDD:'))

            numero = ouvir_microfone()
            print('numero: ' + numero)

            return mensagens.enviar_zap(mensagem, numero)
        except:
            print('Erro - Microfone')
            return 'Erro no envio!'        
    elif len(texto) > 0:
        return wikipedia.resumo(texto)    

def main():
    COMANDOS_FINALIZAR = ['sair', 'fechar', 'desligar']
    audio = ''

    aprensentacao = """
                    Olá, eu sou a assistente virtual!
                    """

    aprensentacao = 'Olá Fale'
    
    print(aprensentacao)
    asyncio.run(gerar_audio(aprensentacao))

    while True:
        
        try:
            pergunta = 'Em que posso ajudar?'
            print(pergunta)
            asyncio.run(gerar_audio(pergunta))

            audio = ouvir_microfone()
            print('Audio: ' + audio)
        except:
            print('Erro - Microfone') 
            audio = ''

        if len(audio) > 0:
            asyncio.run(gerar_audio(audio))
            if (bool([comando for comando in COMANDOS_FINALIZAR if(comando in audio.lower())])):
                break
            else:
                comando = executar_comando(audio)
                if comando:            
                    asyncio.run(gerar_audio(comando))

print("SISTEMA DE RECONHECIMENTO POR VOZ")
main()