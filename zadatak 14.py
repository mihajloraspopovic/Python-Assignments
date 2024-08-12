velicina = float(input("Unesite veličinu stana u kvadratnim metrima: "))
zona = int(input("Unesite zonu lokacije (1, 2, 3): "))
parking = int(input("Da li stan ima parking? (1 = da, 0 = ne): "))

cena_po_kvadratu = 1200
fiksna_cena_ucesca = 1000

osnovna_cena = velicina * cena_po_kvadratu

cena_lokacije = zona * 5 * velicina
cena_parkinga = parking * 10 * zona * velicina

ukupna_cena = osnovna_cena + cena_lokacije + cena_parkinga + fiksna_cena_ucesca

print(f"Konačna cena stana je: {ukupna_cena:.2f} evra")
