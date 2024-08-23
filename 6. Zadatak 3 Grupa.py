class Televizor:
    def __init__(self, broj_tekuci_kanal=0, naziv_tekuci_kanal="", jačina_tona=5):
        self._broj_tekuci_kanal = broj_tekuci_kanal
        self._naziv_tekuci_kanal = naziv_tekuci_kanal
        self._kanali = []
        self._jačina_tona = jačina_tona

    @property
    def broj_tekuci_kanal(self):
        return self._broj_tekuci_kanal

    @broj_tekuci_kanal.setter
    def broj_tekuci_kanal(self, value):
        if 0 <= value < len(self._kanali):
            self._broj_tekuci_kanal = value
            self._naziv_tekuci_kanal = self._kanali[value]

    @property
    def naziv_tekuci_kanal(self):
        return self._naziv_tekuci_kanal

    @property
    def kanali(self):
        return self._kanali

    @property
    def jačina_tona(self):
        return self._jačina_tona

    @jačina_tona.setter
    def jačina_tona(self, value):
        if 0 <= value <= 10:
            self._jačina_tona = value

    def dodaj_kanal(self, naziv_kanala):
        self._kanali.append(naziv_kanala)

    def obriši_kanal(self, naziv_kanala):
        if naziv_kanala in self._kanali:
            self._kanali.remove(naziv_kanala)

    def pojačaj_ton(self):
        if self._jačina_tona < 10:
            self._jačina_tona += 1

    def ime_kanala(self, broj_kanala):
        if 1 <= broj_kanala <= len(self._kanali):
            return self._kanali[broj_kanala - 1]
        return None
