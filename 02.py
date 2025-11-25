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