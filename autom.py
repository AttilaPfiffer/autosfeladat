from Auto import Autok

autolista = []
fajlom = open("auto.txt", "r", encoding = "UTF-8")
fajlom.readline()
lista = fajlom.readlines()
fajlom.close()
for i in range(0, len(lista), 1):
    aktsor: int = lista[i].strip()
    print(aktsor)
    sor_lista = aktsor.split("$")
    print(sor_lista[0])
    print(sor_lista[1])
    autok = Autok(sor_lista[0], int(sor_lista[1]))
    autolista.append(autok)

for i in range(0, len(autolista), 1):
    print(f"{autolista[i].nev}, {autolista[i].gyart_datum}")

def flotta():
    print("III/Flotta")
    db: int = 0
    for i in range(0, len(autolista), 1):
        db += i
    return db