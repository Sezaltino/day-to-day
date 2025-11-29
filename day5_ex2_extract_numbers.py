''''
📋 Contexto
Você recebeu um relatório em formato de texto e precisa extrair todos os números dele para análise estatística.
🎯 Objetivo
Crie uma função extrair_numeros(texto) que retorne uma lista com todos os números encontrados no texto (como strings ou inteiros).
📥 Entrada Esperada
pythontexto = "A empresa vendeu 150 unidades em 2024, com lucro de 45% e crescimento de 12.5 pontos."
📤 Saída Esperada (versão simples)
python['150', '2024', '45', '12', '5']  # ou [150, 2024, 45, 12, 5]
'''
import re

def scraper_numbers(phrase):

    return list(word for word in re.sub("[!?.,:;%]", " ", phrase).split() if word.isdigit())
    #return list(x for x in phrase if x.isdigit())


if __name__ == "__main__":
    pythontext = "A empresa vendeu 150 unidades em 2024, com lucro de 45% e crescimento de 12.5 pontos."    


    print("\nprimeira forma")
    print(scraper_numbers(pythontext))
    print("\nsegunda forma")
    print(list(filter(lambda x: x.isdigit(), re.sub("[!?.,:;%]", " ", pythontext).split())))