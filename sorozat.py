import random
random_szamok: int = []

def feladat2():
    print("II/A, B, C")
    print(f"\t", end = " ")
    for i in range(0, 5, 1):
        szam_sorozat: int = random.randint(0, 100)
        random_szamok.append(szam_sorozat)
        if i < 4:
            print(f"{szam_sorozat}", end = "; ")
        else:
            print(f"{szam_sorozat}", end = " ")
    return random_szamok

def konzol_kiir():
    print("II/D, E")
    egyjegyuek_szama:int = 0
    for i in range(0, len(random_szamok), 1):
        if random_szamok[i] < 10:
            egyjegyuek_szama += 1
    return egyjegyuek_szama

def file_kiir(egyjegyuek):
    f = open("szamok.txt", "a", encoding="UTF-8")
    f.write(f"II/F:\n\tAz egyjegyűek száma: {egyjegyuek}")