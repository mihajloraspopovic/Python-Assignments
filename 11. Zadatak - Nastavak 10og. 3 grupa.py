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


class AlphaColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self._alpha = alpha

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if 0 <= value <= 1:
            self._alpha = value
        else:
            print("Vrijednost za alpha mora biti između 0 i 1.")

    def update_color_by_alpha(self, alpha):
        self.red = max(0, min(255, self.red - self.red * alpha))
        self.green = max(0, min(255, self.green - self.green * alpha))
        self.blue = max(0, min(255, self.blue - self.blue * alpha))

    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}, alpha: {self.alpha}"


alpha_color1 = AlphaColor(200, 150, 100, 0.5)
alpha_color2 = AlphaColor(50, 75, 100, 0.8)

print(alpha_color1)
print(alpha_color2)

alpha_color1.update_color_by_alpha(0.3)
alpha_color2.update_color_by_alpha(0.1)

print(alpha_color1)
print(alpha_color2)
