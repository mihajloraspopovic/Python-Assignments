import math

x1, y1 = map(int, input("Unesite koordinate starog hrasta (x1, y1): ").split())
x2, y2 = map(int, input("Unesite koordinate stare kuce (x2, y2): ").split())

x_b = x2 + 2
y_b = y2 - 3

print(f"Koordinate blga su ({x_b}, {y_b})")

d_vazdusno = math.sqrt((x_b - x1) ** 2 + (y_b - y1) ** 2)
print(f"Vazdusno rastojanje od hrasta do blaga je {d_vazdusno:.2f}")

d_hrast_kuca = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
d_kuca_blago = math.sqrt((x_b - x2)** 2 + (y_b - y2) ** 2)
d_ukupno = d_hrast_kuca + d_kuca_blago

print(f"Ukupno rastojanje od hrasta do blaga preko kuce je {d_ukupno:.2f}")