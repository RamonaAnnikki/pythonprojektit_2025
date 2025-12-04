# Kysytään käyttäjältä minuutit kokonaislukuna
minuutit = input("Anna minuutit: ")

# Muutettaan syöte kokonaisluvuksi
minuutit = int(minuutit)

# Lasketaan tunnit ja jäljelle jäävät minuutit
tunnit = minuutit // 60
jäljelle_minuutit = minuutit % 60

# Tulostetaan tunnit ja minuttit samalla rivillä
print(f"{tunnit}h ja {jäljelle_minuutit}min" )