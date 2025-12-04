# Ohjelma luokan koetulosten keskiarvon ja sanallisen arvion laskemiseen

while True:
    try:
        oppilaat = int(input("Anna oppilaiden lukumäärä: "))
        if oppilaat <= 0:
            print("Oppilasmäärän täytyy olla positiivinen.")
            continue
        break
    except ValueError:
        print("Anna kokonaisluku, kiitos.")

summa = 0  # koetulosten summa

for i in range(1, oppilaat + 1):
    while True:
        try:
            arvosana = float(input(f"Anna oppilaan {i} arvosana (0–5): "))
            if 0 <= arvosana <= 5:
                summa += arvosana
                break
            else:
                print("Arvosanan täytyy olla välillä 0–5.")
        except ValueError:
            print("Anna numeroarvo, kiitos.")

# Lasketaan keskiarvo
keskiarvo = summa / oppilaat
print(f"\nLuokan keskiarvo on {keskiarvo:.2f}")

# Määritetään sanallinen arvio
if 0 <= keskiarvo < 1:
    arvio = "Huono tulos"
elif 1 <= keskiarvo < 2:
    arvio = "Heikko tulos"
elif 2 <= keskiarvo < 3:
    arvio = "Tyydyttävä tulos"
elif 3 <= keskiarvo < 4:
    arvio = "Hyvä tulos"
else:
    arvio = "Kiitettävä tulos"

print("Sanallinen arvio:", arvio)

