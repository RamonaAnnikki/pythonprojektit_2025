import math  # Tarvitaan pallon tilavuuden laskuun

# a) Suorakulmaisen särmiön tilavuus
print("Suorakulmaisen särmiön tilavuus")

a = float(input("Anna särmiön sivu a: "))
b = float(input("Anna särmiön sivu b: "))
c = float(input("Anna särmiön sivu c: "))

V_sarmiö = a * b * c
print(f"Särmiön tilavuus: {V_sarmiö}")

# b) Pallon tilavuus
print("\nPallon tilavuus")

r = float(input("Anna pallon säde: "))
V_pallo = (4/3) * math.pi * r**3

# Pyöristetään kahteen desimaaliin
V_pallo = round(V_pallo, 2)
print(f"Pallon tilavuus: {V_pallo}")