d = int(input("Unesite duzinu terena: "))
s = int(input("Unesite sirinu terena: "))
r = int(input("Unesite rastojanje ograde od terena:"))

d_og = d + 2 * r
s_og = s + 2 * r

duzina_ograde = 2 * (d_og + s_og)

print(f"Duzina ograde je {duzina_ograde} metara.")