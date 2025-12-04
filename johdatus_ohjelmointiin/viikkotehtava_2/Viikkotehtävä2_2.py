import math  # Tarvitaan neliöjuuren laskuun

print("Suorakulmaisen kolmion hypotenuusan laskenta")

# Kysy käyttäjältä kateettien pituudet
a = float(input("Anna ensimmäisen kateetin pituus: "))
b = float(input("Anna toisen kateetin pituus: "))

# Laske hypotenuusa
c = math.sqrt(a**2 + b**2)

# Tulosta tulos
print(f"Hypotenuusan pituus on: {c:.2f}")