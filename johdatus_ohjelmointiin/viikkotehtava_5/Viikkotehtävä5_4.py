# Luodaan lista kaupungeista
kaupungit = ["Rooma", "Ateena", "Tukholma", "Lontoo", "Dublin", "Pariisi"]

# Järjestetään lista aakkosjärjestykseen
kaupungit.sort()

# Tulostetaan kaupungit silmukassa rivinumeron kanssa
for i, kaupunki in enumerate(kaupungit, start=1):
    print(f"{i}. {kaupunki}")
