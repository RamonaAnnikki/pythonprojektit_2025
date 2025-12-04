# Kysytään käyttäjältä vuotta
vuosi = int(input("Anna vuosi: "))

# Tarkistetaan, onko vuosi karkausvuosi
karkausvuosi = (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0)

# Tulostetaan tulos
if karkausvuosi:
    print(vuosi, "on karkausvuosi.")
else:
    print(vuosi, "ei ole karkausvuosi.")
