from classok import Film
file = open("film.txt","r", encoding="utf8")
file_lista = file.readlines()[1:]
filmek_lista = []
file.close()
 
#cim,rendezo,foszereplo,ev,perc
def beolvas(file_lista):
    for i in range (0,len(file_lista),1):
        jelen_sor = file_lista[i]
        tisztitott = jelen_sor.strip().split(";")
        cim = tisztitott[0]
        rendezo = tisztitott[1]
        foszereplo = tisztitott[2]
        ev:int = int(tisztitott[3])
        perc:int = int(tisztitott[4])
        filmek = Film(cim,rendezo,foszereplo,ev,perc)
        filmek_lista.append(filmek)
    return filmek_lista
beolvas(file_lista)

def legrovidebb(filmek_lista):
    hossz_lista = []
    legrovidebb_nev = ""
    for i in range (0,len(filmek_lista),1):
        hossz_lista.append(filmek_lista[i].perc)
    hossz_lista.sort()
    legrovidebb:int = int(min(hossz_lista))
    for i in range (0,len(filmek_lista),1):
        if filmek_lista[i].perc == legrovidebb:
            legrovidebb_nev = filmek_lista[i].cim
    print(f"A legrövidebb film címe: {legrovidebb_nev}")

def szaztizperc(filmek_lista):
    szaztizperces_filmek = 0
    for i in range (0,len(filmek_lista),1):
        if filmek_lista[i].perc >= 110:
            szaztizperces_filmek += 1
    print (f"{szaztizperces_filmek} film legalább 110 perces")

def szineszkereso(filmek_lista):
    szinesz_nev = input("Adjon meg egy színész nevet")
    szinesz_nevek = []
    for i in range (0,len(filmek_lista),1):
        szinesz_nevek.append(filmek_lista[i].foszereplo)
        if filmek_lista[i].foszereplo == szinesz_nev:
            print(f"{filmek_lista[i].cim}")
    if szinesz_nev not in szinesz_nevek:
        print("Nem található ilyen színész, kérem próbálja urja később")
szineszkereso(filmek_lista)