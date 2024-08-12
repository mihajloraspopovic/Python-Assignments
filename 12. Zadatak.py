from datetime import datetime

N = int(input("Unesite koliko godina ima Milos:"))

trenutna_godina = datetime.now().year

godina_rodjenja = trenutna_godina - N

print(f"MMilos je rodjen {godina_rodjenja}.")