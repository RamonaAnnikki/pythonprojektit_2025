# import datetime, halutaan käyttää kirjastosta VAIN
# näitä objekteja
from datetime import date, datetime


# Tällä tuodaan haluttu kirjasto, ko. koodin käyttöön.
# Näin pystyt käyttämään haluttuja komentosanoja

# Datetime sisältää date objektin ja tällä on fuktio
# nimeltään today
# Eli nyt koodia pitää muuttaa niin, että halutaan vain
# date ja today, eli dat.today. Aiemmin oli today = datetime.date.today()
today = date.today()
print(today.year, today.month, today.day)

# Jos tarvitset päivämäärän lisäksi kellonaikaa, niin
# silloin kannattaa käyttää datetime kirjaston sisältä
# datetime nimistä objektia ja sen now() funktiota
current_time = datetime.now()
# tämäkin täytyi koodissa muuttaa, se oli aiemmin current_time = datetime.datetime.now()
print(current_time)

# Jos halutaan muokata tulostusinformaattia omanlaiseksi,
# niin voit käyttää strftime() nimistä funktiota
formatted_time = current_time.strftime("%d.%m.%y klo %H:%M")
# prosentti ja kirjain tarkoittaa, päivä, kuukausi, vuosi jne. %y on -25 ja %Y on 2025
print(formatted_time)



