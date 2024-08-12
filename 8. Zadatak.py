import math

def duzina_trake(povrsina): 
  poluprecnik = math.sqrt(povrsina / math.pi)

  obim = 2 * math.pi * poluprecnik

  return obim

povrsina = float(input("Unesite površinu stolnjaka: "))

duzina = duzina_trake(povrsina)

print(f"Potreba duzina trake za ivicu stolnjaka je {duzina:.2f} m.")
