import math

ympyran_sade = input("Anna ympyrän säde: ")
sivun_pituus = input("Syötä neliön sivun pituus: ")

ympyran_pinta = math.pi * float(ympyran_sade) ** 2
neliö_ala = float(sivun_pituus) ** 2

print(f"pyrän pinta ala on {ympyran_pinta:.2f}")
print(f"neliön pinta ala on {neliö_ala:.2f}")

