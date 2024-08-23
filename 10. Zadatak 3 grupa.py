class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        if 0 <= value <= 255:
            self._red = value
        else:
            print("Vrijednost za red mora biti između 0 i 255.")

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        if 0 <= value <= 255:
            self._green = value
        else:
            print("Vrijednost za green mora biti između 0 i 255.")

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        if 0 <= value <= 255:
            self._blue = value
        else:
            print("Vrijednost za blue mora biti između 0 i 255.")

    def add_red(self, change):
        self._red = max(0, min(255, self._red + change))

    def add_green(self, change):
        self._green = max(0, min(255, self._green + change))

    def add_blue(self, change):
        self._blue = max(0, min(255, self._blue + change))

    def __lt__(self, other):
        return (self.red < other.red and
                self.green < other.green and
                self.blue < other.blue)

    def __eq__(self, other):
        return (self.red == other.red and
                self.green == other.green and
                self.blue == other.blue)

    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"

color1 = Color(100, 150, 200)
color2 = Color(120, 160, 210)

print(color1)
print(color2)

print(color1 < color2)
print(color1 == color2)

color1.add_red(-50)
color1.add_green(100)
color1.add_blue(-300)

print(color1)
