import random
import string

# Mahdolliset merkit
pienet = string.ascii_lowercase
isot = string.ascii_uppercase
numerot = string.digits
erikoismerkit = "-_~?*$#!+%@"

while True:
    try:
        pituus = int(input("Kuinka pitkä salasana halutaan? (vähintään 8): "))
        if pituus < 8:
            print("Salasanan täytyy olla vähintään 8 merkkiä pitkä.")
            continue
        break
    except ValueError:
        print("Anna numero, kiitos.")

# Rakennetaan salasana, jossa on vähintään yksi jokaisesta ryhmästä
salasana = [
    random.choice(pienet),
    random.choice(isot),
    random.choice(numerot),
    random.choice(erikoismerkit)
]

# Täydennetään loppuosa satunnaisilla merkeillä kaikista ryhmistä
kaikki_merkit = pienet + isot + numerot + erikoismerkit
for _ in range(pituus - 4):
    salasana.append(random.choice(kaikki_merkit))

# Sekoitetaan merkkien järjestys
random.shuffle(salasana)

# Muutetaan lista merkkijonoksi
salasana = "".join(salasana)

print(f"\nLuotu turvallinen salasana: {salasana}")
