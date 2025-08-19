banaani = input("Anna banaaninen määrä (kg): ")
appelsiini = input("Anna appelsiinien määrä (kg): ")
omena = input("Anna omenien määrä (kg): ")

banaani_kilohinta = 2.85
appelsiini_kilohinta = 3.15
omena_kilohinta = 4.05

banaani_hinta =  float(banaani) * banaani_kilohinta
appelsiini_hinta = float(appelsiini) * appelsiini_kilohinta
omena_hinta = float(omena) * omena_kilohinta

print("Ostosten yhteenveto:")
print(f"banaani: {banaani_hinta:.2f}€")
print(f"appelsiini: {appelsiini_hinta:.2f}€")
print(f"omena: {omena_hinta:.2f}€")
print(f"{banaani_hinta+appelsiini_hinta+omena_hinta}€")
