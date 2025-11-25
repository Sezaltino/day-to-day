'''
Dia 3 – Contagem de Palavras
📋 Contexto
Você está analisando feedbacks de clientes e precisa descobrir quais palavras aparecem com mais frequência para identificar padrões.
🎯 Objetivo
Crie uma função contar_palavras(texto) que receba um texto e retorne um dicionário com a contagem de cada palavra.
📥 Entrada Esperada
pythontexto = "python é legal python é poderoso e python é muito usado"
📤 Saída Esperada
python{
    'python': 3,
    'é': 3,
    'legal': 1,
    'poderoso': 1,
    'e': 1,
    'muito': 1,
    'usado': 1
}
'''

def contagem_palavras(text):
    text_split = text.split(" ")
    analyze = {}
    for word in text_split:
        print(word)
        if analyze.get(word) is not None:
            print(analyze.get(word))
            analyze[word]+=1
        else:
            analyze[word]=1

    print(analyze)
    return analyze
    





if __name__ == "__main__":
    #pythontexto = input("Digite sua frase: ")
    pythontexto = "python é legal python é poderoso e python é muito usado"
    contagem_palavras(pythontexto)