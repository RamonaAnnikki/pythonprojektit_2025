# Kysytään käyttäjältä automatkan pituus kilometreinä
matka = input("Anna matkan pituus kilometreineä: ")

# Muutetaan syöte desimaaliluvuksi
matka = float(matka)

# Polttoaineen kulutus 6.5 litraa per 100 km
kulutus_per_100km = 6.5

# Lasketaan arvioitu kokonaiskulutus
kulutus = matka * kulutus_per_100km / 100

# Tulostetaan kulutus yhden desimaalin tarkkuudella
print(f"Arvioitu polttoaineen kulutus: {kulutus:.1f} litraa")

