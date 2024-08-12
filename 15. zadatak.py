import math

x1, y1 = map(float, input("Unesite koordinate tačke A (x1, y1): ").split())
x2, y2 = map(float, input("Unesite koordinate tačke B (x2, y2): ").split())
x3, y3 = map(float, input("Unesite koordinate tačke C (x3, y3): ").split())

a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

s = (a + b + c) / 2

povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Površina trougla je: {povrsina:.2f}")

