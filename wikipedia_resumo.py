import wikipedia

def resumo(chave):
    try:
        print('Wikipedia')
        wikipedia.set_lang("pt")
        return wikipedia.summary(chave, sentences=1)
    except:
        print('Erro - Wikipedia')
        return 'Erro na busca'