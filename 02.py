def formatter(name):
    name = name.casefold()
    name = name.strip()
    name = name.capitalize()
    return name

def normalize_name(names):

    names_filted = []
    condition = False

    for name in names:
        for letter in name:
            if condition:
                continue
            condition = True if letter.isdigit() else False

        if not condition:
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
