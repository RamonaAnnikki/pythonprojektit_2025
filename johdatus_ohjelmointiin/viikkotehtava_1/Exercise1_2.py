# Kysytään käyttäjältä tuotteen hinta ilman ALV:ia
hinta_ilman_alv = input("Anna tuotteen hinta ilman ALV:ia:")

# Muutetaan syöte desimaaliluvuksi
hinta_ilman_alv = float(hinta_ilman_alv)

# Lasketaan hinta ALV:n kanssa (24%)
alv_prosentti = 24
hinta_alv = hinta_ilman_alv * (1 + alv_prosentti / 100)

# Tulostetaan lopputulos kahdella desimaalilla
print(f"Tuotteen hinta ALV:n kanssa {hinta_alv:.2f} €")
