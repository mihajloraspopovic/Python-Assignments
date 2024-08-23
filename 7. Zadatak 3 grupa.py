class Book:
    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self._naslov = naslov
        self._autor = autor
        self._godina_izdanja = godina_izdanja
        self._broj_kopija = broj_kopija

    @property
    def naslov(self):
        return self._naslov

    @naslov.setter
    def naslov(self, value):
        self._naslov = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def godina_izdanja(self):
        return self._godina_izdanja

    @godina_izdanja.setter
    def godina_izdanja(self, value):
        self._godina_izdanja = value

    @property
    def broj_kopija(self):
        return self._broj_kopija

    @broj_kopija.setter
    def broj_kopija(self, value):
        self._broj_kopija = value


class Library:
    def __init__(self):
        self.knjige = []

    def dodaj_knjigu(self, knjiga):
        self.knjige.append(knjiga)

    def obriši_knjigu(self, naslov):
        for knjiga in self.knjige:
            if knjiga.naslov == naslov:
                self.knjige.remove(knjiga)
                return True
        return False

    def pretraga_po_naslovu(self, naslov):
        rezultat = []
        for knjiga in self.knjige:
            if naslov.lower() in knjiga.naslov.lower():
                rezultat.append(knjiga)
        return rezultat

    def pretraga_po_autoru(self, autor):
        rezultat = []
        for knjiga in self.knjige:
            if autor.lower() in knjiga.autor.lower():
                rezultat.append(knjiga)
        return rezultat

    def prikaz_svih_knjiga(self):
        for knjiga in self.knjige:
            print(f"Naslov: {knjiga.naslov}, Autor: {knjiga.autor}, Godina izdanja: {knjiga.godina_izdanja}, Broj kopija: {knjiga.broj_kopija}")


def glavni_program():
    biblioteka = Library()

    while True:
        print("\nOpcije:")
        print("1. Dodaj knjigu")
        print("2. Prikaz svih knjiga")
        print("3. Uredi knjigu")
        print("4. Obriši knjigu")
        print("5. Pretraga po naslovu")
        print("6. Pretraga po autoru")
        print("7. Izlaz")

        opcija = input("Izaberite opciju: ")

        if opcija == "1":
            naslov = input("Unesite naslov knjige: ")
            autor = input("Unesite autora knjige: ")
            godina_izdanja = input("Unesite godinu izdanja knjige: ")
            broj_kopija = int(input("Unesite broj kopija: "))
            knjiga = Book(naslov, autor, godina_izdanja, broj_kopija)
            biblioteka.dodaj_knjigu(knjiga)

        elif opcija == "2":
            biblioteka.prikaz_svih_knjiga()

        elif opcija == "3":
            naslov = input("Unesite naslov knjige koju želite urediti: ")
            knjige = biblioteka.pretraga_po_naslovu(naslov)
            if knjige:
                knjiga = knjige[0]
                print("Izmenite informacije o knjizi (ostavite prazno za zadržavanje trenutnih vrednosti):")
                novi_naslov = input(f"Naslov ({knjiga.naslov}): ")
                novi_autor = input(f"Autor ({knjiga.autor}): ")
                nova_godina_izdanja = input(f"Godina izdanja ({knjiga.godina_izdanja}): ")
                novi_broj_kopija = input(f"Broj kopija ({knjiga.broj_kopija}): ")

                if novi_naslov:
                    knjiga.naslov = novi_naslov
                if novi_autor:
                    knjiga.autor = novi_autor
                if nova_godina_izdanja:
                    knjiga.godina_izdanja = nova_godina_izdanja
                if novi_broj_kopija:
                    knjiga.broj_kopija = int(novi_broj_kopija)
            else:
                print("Knjiga nije pronađena.")

        elif opcija == "4":
            naslov = input("Unesite naslov knjige koju želite obrisati: ")
            if biblioteka.obriši_knjigu(naslov):
                print("Knjiga je obrisana.")
            else:
                print("Knjiga nije pronađena.")

        elif opcija == "5":
            naslov = input("Unesite naslov za pretragu: ")
            knjige = biblioteka.pretraga_po_naslovu(naslov)
            for knjiga u knjige:
                print(f"Naslov: {knjiga.naslov}, Autor: {knjiga.autor}, Godina izdanja: {knjiga.godina_izdanja}, Broj kopija: {knjiga.broj_kopija}")

        elif opcija == "6":
            autor = input("Unesite autora za pretragu: ")
            knjige = biblioteka.pretraga_po_autoru(autor)
            for knjiga u knjige:
                print(f"Naslov: {knjiga.naslov}, Autor: {knjiga.autor}, Godina izdanja: {knjiga.godina_izdanja}, Broj kopija: {knjiga.broj_kopija}")

        elif opcija == "7":
            break

        else:
            print("Nepoznata opcija. Pokušajte ponovo.")

if __name__ == "__main__":
    glavni_program()
