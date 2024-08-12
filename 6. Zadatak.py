def kvadrat_trinoma(a, b, c):
  rezultat = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c
  return rezultat

a = float(input("Unesite koeficijent a: "))
b = float(input("Unesite koeficijent b: "))
c = float(input("Unesite koeficijent c: "))

rezultat = kvadrat_trinoma(a, b, c)

print(f"Kvadrat trinoma za a={a}, b={b}, c={c} je: {rezultat}")