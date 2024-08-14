prisustvo = float(input("Unesite procenat prisustva: "))
seminarski = int(input("Unesite 1 ako su svi seminarski radovi predati, 0 ako nije: "))

if prisustvo > 75 and seminarski == 1:
  print("Student može pristupiti ispitu.")
else:
  print("Student ne može pristupiti ispitu.")
