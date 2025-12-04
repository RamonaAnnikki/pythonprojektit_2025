from datetime import date

# Määritellään muuttujat
asiakas = "Anni Sysmäläinen"
syntymavuosi = 1991
saldo = 1525

# Haetaan tämän päivän päivämäärä
tanaan = date.today()

# Muodostetaan päivämäärä haluttuun muotoon (esim. tääpäivä 8.10.2025)
paivamaara = f"{tanaan.day}.{tanaan.month}.{tanaan.year}"

# Yhdistetään tiedot tulostettavaksi
tuloste = (f"{asiakas} ({syntymavuosi}), "
           f"saldo: {saldo} €, päivitetty {paivamaara}.")

# Tulostetaan
print(tuloste)
