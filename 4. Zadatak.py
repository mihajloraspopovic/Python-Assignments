def obim_terena(d, s):
  return 2 * (d + s)

d = float(input("Unesite duzinu terena: "))
s = float(input("Unesite sirinu terena: "))

obim = obim_terena(d, s)

ukupna_distanca = obim * 4

print(f"Sportista ce pretrcati ukupno {ukupna_distanca} metara obilazenjem terena 4 puta.")
