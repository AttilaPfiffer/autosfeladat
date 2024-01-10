import bevezetes
import sorozat
import autom

bevezetes.feladat1()
sorozat.feladat2()
print("\n")
egyjegyuek: int = sorozat.konzol_kiir()
print(f"\tAz egyjegyűek száma: {egyjegyuek}")

print("\n")
sorozat.file_kiir(egyjegyuek)

mennyi = autom.flotta()
print(f"\tAz autók száma: {mennyi}")