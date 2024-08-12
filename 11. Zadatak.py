import math

def euclide_distance(A, B):

  dx = B[0] - A[0]
  dy = B[1] - A[1]

  distance = math.sqrt(dx**2 + dy**2)

  return distance

x1, y1 = map(float, input("Unesite koordinate tacke A (x1 y1): ").split())
x2, y2 = map(float, input("Unesite koordinate tacke B (x2 y2): ").split())

rastojanje = euclide_distance((x1, y1),(x2, y2))
print(f"Euklidsko rastojanje izmedju tacaka A i B je {rastojanje:.2f}.")