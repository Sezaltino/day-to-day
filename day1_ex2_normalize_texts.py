'''
Exercício 2 – Normalizar Textos
📋 Contexto
Você recebeu uma planilha de cadastro de clientes, mas os nomes vieram bagunçados: com espaços extras, letras maiúsculas e minúsculas misturadas. Antes de salvar no banco de dados, você precisa padronizar tudo.
🎯 Objetivo
Crie uma função normalizar_nomes(nomes) que receba uma lista de nomes e retorne uma lista limpa, onde cada nome:

Não tenha espaços no início ou fim
Tenha apenas a primeira letra maiúscula
Esteja em formato consistente

📥 Entrada Esperada
pythonnomes = [
    "  MARIA SILVA  ",
    "joão SANTOS",
    "   Ana   Costa   ",
    "PEDRO oliveira  "
]
📤 Saída Esperada
python["Maria Silva", "João Santos", "Ana Costa", "Pedro Oliveira"]
'''

def normalize_name(names):

    names_filted = []
    names_filted2 = []

    #first solution - not filter number caracter if has
    name_filted_strings = list(name.split() for name in names)
    for name in name_filted_strings:
        names_filted2.append(list(map(lambda x: x.casefold().strip().capitalize(), name)))
    names_filted2 = list(map(lambda x: " ".join(x), names_filted2))

    #second solution - better solution
    for name in names:
        has_digit = any(letter.isdigit() for letter in name)
        if not has_digit:
            final_name = list(word.casefold().strip().capitalize() for word in name.split())
            names_filted.append(" ".join(final_name))
        else:
            names_filted.append(f"name contain numeric caracter")    

    return names_filted

if __name__ == "__main__":
    names = [
        "  Linda Sezaltino  ",
        "PEDRO oliveir4  ",
        "joão SANTOS",
        "   Ana   Costa   ",
        ]
    print(normalize_name(names))