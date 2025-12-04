print("Polttoaineen kulutuksen laskenta")

# Polttoaineen kulutus
matka_kulutus = 5.1  # litraa / 100 km
kaupunki_kulutus = 7.5  # litraa / 100 km

# Kysy käyttäjältä ajokilometrit
matka_km = float(input("Anna matka-ajon kilometrit: "))
kaupunki_km = float(input("Anna kaupunkiajon kilometrit: "))

# Laske kulutus
matka_litraa = matka_km * matka_kulutus / 100
kaupunki_litraa = kaupunki_km * kaupunki_kulutus / 100
yhteensa_litraa = matka_litraa + kaupunki_litraa

# Tulosta tulokset
print(f"Matka-ajon polttoaineen kulutus: {matka_litraa:.2f} litraa")
print(f"Kaupunkiajon polttoaineen kulutus: {kaupunki_litraa:.2f} litraa")
print(f"Yhteensä polttoainetta kuluu: {yhteensa_litraa:.2f} litraa")