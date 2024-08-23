import random

class Turnir:
    def __init__(self, naziv_turnira, broj_rundi):
        self._naziv_turnira = naziv_turnira
        self._lista_igrača = []
        self._broj_rundi = broj_rundi
        self._odigrane_runde = 0

    @property
    def naziv_turnira(self):
        return self._naziv_turnira

    @naziv_turnira.setter
    def naziv_turnira(self, value):
        self._naziv_turnira = value

    @property
    def lista_igrača(self):
        return self._lista_igrača

    @lista_igrača.setter
    def lista_igrača(self, value):
        self._lista_igrača = value

    @property
    def broj_rundi(self):
        return self._broj_rundi

    @broj_rundi.setter
    def broj_rundi(self, value):
        if 0 < value < 10:
            self._broj_rundi = value

    @property
    def odigrane_runde(self):
        return self._odigrane_runde

    def dodaj_igrača(self, ime_igrača):
        self._lista_igrača.append((ime_igrača, 0))

    def obriši_igrača(self, ime_igrača):
        self._lista_igrača = [igrač for igrač in self._lista_igrača if igrač[0] != ime_igrača]

    def prikazi_najboljeg_igrača(self):
        if not self._lista_igrača:
            return "Nema igrača u turniru"
        najbolji_igrač = max(self._lista_igrača, key=lambda igrač: igrač[1])
        return najbolji_igrač[0]

    def pokreni_rundu(self):
        if len(self._lista_igrača) < 2:
            return "Nedovoljno igrača za rundu"

        igrač1, igrač2 = random.sample(self._lista_igrača, 2)
        vjerovatnoća = 0.6 if igrač1[1] > igrač2[1] else 0.4

        if random.random() < vjerovatnoća:
            pobjednik, gubitnik = igrač1, igrač2
        else:
            pobjednik, gubitnik = igrač2, igrač1

        pobjednik_index = self._lista_igrača.index(pobjednik)
        self._lista_igrača[pobjednik_index] = (pobjednik[0], pobjednik[1] + 1)
        self._odigrane_runde += 1

        return f"Runda {self._odigrane_runde}: {pobjednik[0]} pobjeđuje protiv {gubitnik[0]}"

turnir = Turnir("Zimski Turnir", 5)

turnir.dodaj_igrača("Marko")
turnir.dodaj_igrača("Ana")
turnir.dodaj_igrača("Ivan")

print(turnir.pokreni_rundu())
print(turnir.pokreni_rundu())
print(turnir.pokreni_rundu())

print("Najbolji igrač je:", turnir.prikazi_najboljeg_igrača())
