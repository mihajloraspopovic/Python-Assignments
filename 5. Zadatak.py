def povrsina_u_cm2(sirina_mm, visina_mm):

  sirina_cm = sirina_mm / 10
  visina_cm = visina_mm / 10

  povrsina_u_cm2 = sirina_cm * visina_cm

  return povrsina_u_cm2

sirina_mm = float(input("Unesite širinu u milimetrima: "))
visina_mm = float(input("Unesite visinu u milimetrima: "))

povrsina = povrsina_u_cm2(sirina_mm, visina_mm)

print(f"Površina u centimetrima kvadratnim je: {povrsina}")