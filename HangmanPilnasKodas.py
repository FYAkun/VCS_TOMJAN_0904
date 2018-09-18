import random
import hangmanwordbank

# apsibreziam kintamuosius kurie visose partijose bus
zaidziam = True
leidziamos_raides = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pergales = 0.0
pralaimejimai = 0.0


# apsibreziam standartines funkcijas
def klaidu_pasirinkimas():
    klaidos = int(input("Iveskite kiek kartu leidziama suklysti (3-6): "))
    while klaidos > 6 or klaidos < 3:
        klaidos = int(input("Iveskite kiek kartu leidziama suklysti (3-6): "))
    return klaidos


def lygio_pasirinkimas():
    lygis = int(input("Pasirinkite lygi:"))
    while lygis <= 3 or lygis >= 9:
        lygis = int(input("Pasirinkite lygi:"))
    return lygis


def temos_pasirinkimas():
    tema = int(input("Pasirinkite tema: \n 1 - Dazniausi anglu kalbos zodziai \n 2 - Masinos dalys \n 3 - Gyvunai"))
    while tema < 1 or tema > 3:
        tema = int(input("Pasirinkite tema: \n 1 - Dazniausi anglu kalbos zodziai \n 2 - Masinos dalys \n 3 - Gyvunai"))
    if tema == 1:
        sarasas = "zodziu_sarasas.txt"
        return sarasas
    elif tema == 2:
        sarasas = "carparts.txt"
        return sarasas
    else:
        sarasas = "animals.txt"
        return sarasas


def zodzio_isrinkimas(sarasas):
    failo_objektas = open(sarasas, "r")
    for zodis in failo_objektas.readlines():
        zodzio_ilgis = zodis.__len__() - 1  # -1, nes \n suprantamas kaip 1 simbolis
        if lygis >= zodzio_ilgis and zodzio_ilgis >= 3:
            zodziu_sarasas.append(zodis.replace("\n", ""))
            zodis_kuri_spet = random.choice(zodziu_sarasas)
    return zodis_kuri_spet


while zaidziam == True:
    # apsibreziam kintamuosius, kurie kiekvienai partijai bus nauji
    sarasas = ""
    zodziu_sarasas = []
    klaidos = klaidu_pasirinkimas()
    lygis = lygio_pasirinkimas()

    while sarasas == "":
        try:
            sarasas = temos_pasirinkimas()
        except ValueError:
            print("Temai pasirinkti galima naudoti tik skaicius.")

    zodis_kuri_spet = zodzio_isrinkimas(sarasas)
    zaidimo_momentas = 6 - klaidos
    raidziu_skaicius = zodis_kuri_spet.__len__()
    pasleptas_zodis = " _" * raidziu_skaicius
    spejimai = []
    atspetos_raides = 0
    pasikartojantis_spejimas = 0
    #   print(zodis_kuri_spet) #sanity check
    print("Zodis sudarytas is ", raidziu_skaicius, " raidziu")
    print(pasleptas_zodis)
    partija = True
    while partija == True:
        # print(atspetos_raides) #sanity check
        if atspetos_raides == zodis_kuri_spet.__len__():
            print("Sveikiname, jus laimejote")
            pergales = pergales + 1
            break
        elif zaidimo_momentas == 6:
            print("Deja, jus pralaimejote, zodis buvo - ", zodis_kuri_spet)
            pralaimejimai = pralaimejimai + 1
            break
        else:
            spejimas = input("Spekite raide: ")
            if spejimas.__len__() != 1:
                print("Ivedete per daug simboliu")
                continue
            elif spejimas not in leidziamos_raides:
                print("Ivestas simbolis nera raide.")
                continue
            else:
                if spejimas in spejimai:
                    # zaidimo_momentas neaprasytas (nes funkcija anksciau uz kintamojo ivedima)
                    if pasikartojantis_spejimas == 0:
                        print("Sia raide jau spejote, taciau pirma karta klaida neskaiciuojama")
                        pasikartojantis_spejimas = pasikartojantis_spejimas + 1
                        spejimai.append(spejimas)
                    else:
                        print("Sia raide jau spejote, tai skaiciuojama kaip klaida")
                        zaidimo_momentas = zaidimo_momentas + 1
                        hangmanwordbank.Piesimas(zaidimo_momentas)
                        print(pasleptas_zodis)
                elif spejimas in zodis_kuri_spet:
                    print("Raide zodyje yra")
                    spejimai.append(spejimas)
                    pasikartojimas = zodis_kuri_spet.count(spejimas)
                    atspetos_raides = atspetos_raides + pasikartojimas
                    for i, c in enumerate(zodis_kuri_spet):
                        if spejimas == c:
                            pasleptas_zodis = pasleptas_zodis[:2 * i + 1] + spejimas + pasleptas_zodis[2 * i + 2:]
                    print(pasleptas_zodis)
                    continue
                else:
                    print("Tokios raides zodyje nera")
                    spejimai.append(spejimas)
                    zaidimo_momentas = zaidimo_momentas + 1
                    hangmanwordbank.Piesimas(zaidimo_momentas)
                    print(pasleptas_zodis)
                    continue
    # sitas for fun itrauktas
    laimejimu_procentas = (pergales / (pergales + pralaimejimai)) * 100
    print("Siuo metu jusu rezultatas: ", pergales, " pergales ", pralaimejimai, " pralaimejimai ", laimejimu_procentas,
          " % laimejimai")
    atsakymas = input("Ar norite zaisti dar karta:(y/n) ?")
    if atsakymas == "y":
        continue
    else:
        zaidziam = False
