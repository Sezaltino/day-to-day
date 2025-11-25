def formatter(name):
    name = name.casefold().strip().capitalize()
    return name

def normalize_name(names):

    names_filted = []
    names_filted2 = []
    condition = False

    #first solution
    name_filted_strings = list(name.split() for name in names)
    for name in name_filted_strings:
        names_filted2.append(list(map(lambda x: x.casefold().strip().capitalize(), name)))
    names_filted2 = list(map(lambda x: " ".join(x), names_filted2))

    #second solution
    for name in names:
        for letter in name:
            if condition:
                continue
            condition = True if letter.isdigit() else False

        if not condition:
            #TODO rever algoritmo para identificar mais de 2 nomes (ideia full_name = name.split())
            name = name.split()
            first_name = name[0]
            last_name = name[1]
            names_filted.append(formatter(first_name)+ " " +formatter(last_name))

        else:
            names_filted.append(f"name contain numeric caracter")    
    return names_filted

if __name__ == "__main__":
    names = [
        "  Linda Sezaltino  ",
        "joão SANTOS",
        "   Ana   Costa   ",
        "PEDRO oliveir4  "
        ]
    print(normalize_name(names))