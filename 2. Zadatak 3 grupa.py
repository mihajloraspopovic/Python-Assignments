from itertools import groupby
from functools import reduce
import operator

def max_proizvod_podniz(arr):
    max_proizvod = 0
    max_sekvenca = []

    for kljuc, grupa in groupby(arr):
        sekvenca = list(grupa)
        if len(sekvenca) > 1:
            proizvod = reduce(operator.mul, sekvenca, 1)
            if proizvod > max_proizvod:
                max_proizvod = proizvod
                max_sekvenca = sekvenca

    return max_sekvenca, max_proizvod

# Primer korišćenja
arr = [1, 2, 2, 2, 4, 4]
sekvenca, proizvod = max_proizvod_podniz(arr)
print("Sekvenca:", sekvenca)
print("Proizvod:", proizvod)