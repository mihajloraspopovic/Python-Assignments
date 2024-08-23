podcasti = [
    {'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10},
    {'naziv': 'Philosophize This!', 'br_pozitivni': 500, 'br_negativni': 30},
    {'naziv': 'Science VS.', 'br_pozitivni': 600, 'br_negativni': 45}
]

najgori_odnos = None
najgori_podcast = None

for podcast in podcasti:
    odnos = podcast['br_pozitivni'] / podcast['br_negativni']
    if najgori_odnos is None or odnos < najgori_odnos:
        najgori_odnos = odnos
        najgori_podcast = podcast['naziv']

print(najgori_podcast)
