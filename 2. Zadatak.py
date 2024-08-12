import math


def resi_kvadratnu_jednacinu(a, b, c):
  D = b**2 - 4 * a * c


  if D < 0:
    return("Jednacina nema realna resenja")

  sqrt_D = math.sqrt(D)
  x1 = (-b + sqrt_D) / (2 * a)
  x2 = (-b - sqrt_D) / (2 * a)

  return x1, x2

a = float(input("Unesite koeficijent a: "))
b = float(input("Unesite koeficijent b: "))
c = float(input("Unesite koeficijent c: "))

if a == 0:
  print("Koeficijent a ne moze biti za kvadratnu jednacinu")
else:
  rezultat = resi_kvadratnu_jednacinu(a, b, c)

if isinstance(rezultat, str):
  print(rezultat)
else:
  x1, x2 = rezultat
  print(f"Resenja su x1 = {x1} i x2 = {x2}")
