def suma(pirmas, antras):
    if pirmas==int(pirmas) and antras==int(antras):
        atsakymas = pirmas + antras
        return atsakymas
    elif pirmas!=int(pirmas) and antras==int(antras):
        print("pirmas kintamasis nera skaicius")
    elif pirmas==int(pirmas) and antras!=int(antras):
        print("antras kintamasis nera skaicius")
    else:
        print("ne vienas is kintamuju nera skaicius")