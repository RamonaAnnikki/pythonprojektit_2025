# Määritellään muuttujat
paivamaara = "8.10.2019"
asiakas = "Anni Sysmäläinen"
syntymavuosi = 1991
saldo = 1521

# Yhdistetään tiedot yhdeksi tekstiksi
tuloste = (f"{asiakas} ({syntymavuosi}), "
           f"saldo: {saldo} €, päivitetty {paivamaara}.")

# Tulostetaan tiedot
print(tuloste)
