# Pyydetään käyttäjältä kokonaisluku
luku = int(input("Anna kokonaisluku: "))

# Tarkistetaan jaollisuudet
jaollinen_kolmella = (luku % 3 == 0)
jaollinen_viidella = (luku % 5 == 0)

# Tulostetaan tarkempaa tietoa käyttäjälle
if jaollinen_kolmella:
    print(f"Luku {luku} on jaollinen kolmella.")
else:
    print(f"Luku {luku} ei ole jaollinen kolmella.")

if jaollinen_viidella:
    print(f"Luku {luku} on jaollinen viidellä.")
else:
    print(f"Luku {luku} ei ole jaollinen viidellä.")

# Luodaan Boolean-muuttuja, joka kertoo onko luku jaollinen molemmilla
good_division = jaollinen_kolmella and jaollinen_viidella

# Tulostetaan lopputulos
if good_division:
    print("Luku on jaollinen sekä kolmella että viidellä — sopiva!")
else:
    print("Luku ei ole jaollinen sekä kolmella että viidellä — ei sopiva.")
