# Kysytään käyttäjältä 12 kuukauden sademäärät ja lasketaan keskiarvo

kokonais_sade = 0  # tähän kerätään kaikkien kuukausien sademäärät

for i in range(1, 13):  # toistetaan 12 kertaa
    while True:
        try:
            sade = float(input(f"Anna {i}. kuukauden sademäärä (mm): "))
            if sade < 0:
                print("Sademäärä ei voi olla negatiivinen.")
                continue
            kokonais_sade += sade
            break
        except ValueError:
            print("Anna numero, kiitos.")

# lasketaan keskiarvo
keskiarvo = kokonais_sade / 12

# tulostetaan tulos yhdellä desimaalilla
print(f"Vuoden keskimääräinen sademäärä on {keskiarvo:.1f} mm.")
