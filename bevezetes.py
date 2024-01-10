def feladat1():
    print("I/A")
    auto_neve: str = str(input("\tAdja meg az autó nevét: "))
    gyartasi_datum: int = int(input("\tAdja meg a gyártási dátumot: "))


    print("I/B")
    if gyartasi_datum == 2024:
        print(f"\tEz a(z) {auto_neve} friss gyártás.")
    elif gyartasi_datum < 2000:
        print(f"\tEz a(z) {auto_neve} öreg autó.")
    else:
        print(f"\tEz a(z) {auto_neve} átlagos korú.")