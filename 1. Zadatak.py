def povrsina_pravougaonika(duzina, sirina):
  return duzina * sirina

def obim_pravougaonika(duzina, sirina):
  return 2 * (duzina + sirina)

duzina = float(input("Unesite duzinu pravougaonika: "))
sirina = float(input("Unesite sirinu pravougaonika: "))

povrsina = povrsina_pravougaonika(duzina, sirina)
obim = obim_pravougaonika(duzina, sirina)

print(f"Povrsina pravougaonika je: {povrsina}")
print(f"Obim pravougaonika je: {obim}")
