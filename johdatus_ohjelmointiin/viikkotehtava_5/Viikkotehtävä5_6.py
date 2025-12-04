# Luodaan dictionary (sanakirja)
elokuva = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Rikos, Draama",
    "duration": 154
}

# Tulostetaan ilman silmukkaa
print("Ilman silmukkaa:")
print("Nimi:", elokuva["name"])
print("Vuosi:", elokuva["year"])
print("Ohjaaja:", elokuva["director"])
print("Genre:", elokuva["genre"])
print("Kesto:", elokuva["duration"], "min")

print()  # tyhjä rivi väliin

# Tulostetaan silmukalla
print("Silmukalla:")
for avain, arvo in elokuva.items():
    print(f"{avain.capitalize()}: {arvo}")
