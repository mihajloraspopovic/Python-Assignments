import math

def kolicina_vode(time):
  celokupni_sat = math.floor(time)

  litara = celokupni_sat * 0.5

  return litara

time = float(input("Unesite vreme voznje bicikla u satima: "))

litara = kolicina_vode(time)

print(f"Marko ce popiti {int(litara)} litara vode.")
