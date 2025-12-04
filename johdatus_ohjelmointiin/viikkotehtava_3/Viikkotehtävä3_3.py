# Kysytään käyttäjältä työtunnit ja tuntipalkka
tunnit = float(input("Anna työtuntien määrä: "))
tuntipalkka = float(input("Anna tuntipalkka: "))

# Lasketaan viikkopalkka
if tunnit <= 40:
    palkka = tunnit * tuntipalkka
else:
    tavalliset_tunnit = 40
    ylityotunnit = tunnit - 40
    palkka = (tavalliset_tunnit * tuntipalkka) + (ylityotunnit * tuntipalkka * 1.5)

# Tulostetaan palkka
print("Viikkopalkka on:", palkka, "euroa")
