# Assistente Virtual
Assistente Virtual com reconhecimento por voz, possui integração com API OpenWeatherMap para informar a previsão do tempo, integração com o Twilio para envio de mensagens de WhatsApp e com o Wikipédia para pesquisar o resumo de qualquer texto reconhecido pelo assistente, além de iniciar o Chrome e o Excel.

## Executar o Assistente Virtual
python assistente_virtual.py

## Comandos reconhecidos pelo Assistente Virtual:
### Previsão do tempo = ['previsão', 'previsao', 'tempo']
### Envio de mensagens de WhatsApp = ['mensagem', 'zap', 'whatsapp']
### Pesquisa no Wikipédia = ['wikipedia', 'wikipédia', 'pesquisar', 'buscar']
### Abrir o Chrome = 'navegador'
### Abrir o Excel = 'excel'

## Dependências do Assistente Virtual
### SpeechRecognition
### gTTS
### PyAudio
### requests
### Wikipedia
### Twilio
### PyGame
