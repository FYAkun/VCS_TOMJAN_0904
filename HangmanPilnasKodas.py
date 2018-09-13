import random
import hangmanwordbank
#apsibreziam kintamuosius kurie visose partijose bus
zaidziam=True
leidziamos_raides="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#apsibreziam standartines funkcijas
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

def zodzio_isrinkimas():
    failo_objektas=open("zodziu_sarasas.txt", "r")
    for zodis in failo_objektas.readlines():
        zodzio_ilgis = zodis.__len__()-1 # -1, nes \n suprantamas kaip 1 simbolis
        if lygis >= zodzio_ilgis and zodzio_ilgis >=3:
            zodziu_sarasas.append(zodis.replace("\n", ""))
            zodis_kuri_spet = random.choice(zodziu_sarasas)
    return zodis_kuri_spet

    # Kol kas nepavyko iskelti, nes zaidimo_momentas meta NameError
    #    def raide_jau_speta():
    #        if spejimai.count(spejimas) == 1:
    #            print("sia raide jau spejote, taciau pirma karta klaida neskaiciuojama")
    #            spejimai.append(spejimas)
    #        else:
    #            print("sia raide spejote jau keleta kartu, tai skaiciuojama kaip klaida")
    #            zaidimo_momentas = zaidimo_momentas + 1
    #            hangmanwordbank.Piesimas(zaidimo_momentas)
    #            print(pasleptas_zodis)

while zaidziam==True:
    #apsibreziam kintamuosius, kurie kiekvienai partijai bus nauji
    zodziu_sarasas = []
    klaidos=klaidu_pasirinkimas()
    lygis=lygio_pasirinkimas()
    zodis_kuri_spet=zodzio_isrinkimas()
    zaidimo_momentas=6-klaidos
    raidziu_skaicius=zodis_kuri_spet.__len__()
    pasleptas_zodis=" _"*raidziu_skaicius
    spejimai=[]
    atspetos_raides=0
    pasikartojantis_spejimas=0
    #   print(zodis_kuri_spet) #sanity check
    print("Zodis sudarytas is ", raidziu_skaicius, " raidziu")
    print(pasleptas_zodis)

    partija = True
    while partija == True:
        #        print(atspetos_raides) #sanity check
        if atspetos_raides == zodis_kuri_spet.__len__():
            print("Sveikiname, jus laimejote")
            break
        elif zaidimo_momentas == 6:
            print("Deja, jus pralaimejote, zodis buvo - ", zodis_kuri_spet)
            break
        else:
            spejimas=input("Spekite raide: ")
            if spejimas.__len__() != 1:
                print("Ivedete per daug simboliu")
                continue
                #spejimas = input("Spekite raide: ")
            elif spejimas not in leidziamos_raides:
                print("Ivestas simbolis nera raide.")
                continue
                #spejimas = input("Spekite raide: ")
            else:
                if spejimas in spejimai:
#                    raide_jau_speta()
                    if spejimai.count(spejimas) == 1 and pasikartojantis_spejimas==0:
                        print("Sia raide jau spejote, taciau pirma karta klaida neskaiciuojama")
                        pasikartojantis_spejimas=pasikartojantis_spejimas+1
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
                        if spejimas==c:
                            pasleptas_zodis = pasleptas_zodis[:2*i+1] + spejimas + pasleptas_zodis[2*i+2:]
                    print(pasleptas_zodis)
                    continue
                else:
                    print("Tokios raides zodyje nera")
                    spejimai.append(spejimas)
                    zaidimo_momentas=zaidimo_momentas+1
                    hangmanwordbank.Piesimas(zaidimo_momentas)
                    print(pasleptas_zodis)
                    continue

    atsakymas = input("Ar norite zaisti dar karta:(y/n) ?")
    if atsakymas == "y":
        continue
    else:
        zaidziam = False