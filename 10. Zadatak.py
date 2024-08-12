x1, y1 = map(int, input("unesite koordinate gornje lijeve ivice (x1, y1): ").split())
x2, y2 = map(int, input("unesite koordinate donje desne ivice (x2, y2): ").split())

duzina = abs(x2 - x1)
sirina = abs(y2 - y1)

povrsina = duzina * sirina

obim = 2 * (duzina + sirina)

print (f"Povrsina zida je {povrsina}.")
print(f"Obim zida je {obim}.")