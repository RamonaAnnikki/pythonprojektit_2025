# Alkuperäinen teksti
teksti = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Isn’t that neat!"

print("Alkuperäinen teksti:")
print(teksti)
print("-" * 60)

# a) Korvaa sana "fox" sanalla "duck"
teksti = teksti.replace("fox", "duck")
print("a) Sana 'fox' korvattu sanalla 'duck':")
print(teksti)
print("-" * 60)

# b) Pyydetään käyttäjältä sana, joka poistetaan tekstistä
poistettava = input("Anna sana, joka poistetaan tekstistä: ")

if poistettava in teksti:
    teksti = teksti.replace(poistettava, "")
    print("Sana poistettu. Uusi teksti:")
    print(teksti)
else:
    print("Sanaa ei löytynyt.")
print("-" * 60)

# c) Tulostetaan merkkien määrä ja sanojen määrä
merkit = len(teksti)
sanat = len(teksti.split())

print(f"c) Tekstissä on {merkit} merkkiä ja {sanat} sanaa.")
print("-" * 60)

# d) Muutetaan pisteet rivinvaihdoiksi
rivinvaihdettu = teksti.replace(".", "\n")
print("d) Pisteet korvattu rivinvaihdoilla:")
print(rivinvaihdettu)
print("-" * 60)

# e) Lyhennetään teksti 20 merkkiin
if len(teksti) > 20:
    lyhennetty = teksti[:20] + "..."
else:
    lyhennetty = teksti

print("e) Lyhennetty versio:")
print(lyhennetty)
