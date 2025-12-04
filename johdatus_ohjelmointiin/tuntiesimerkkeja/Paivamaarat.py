import datetime
# Tällä tuodaan haluttu kirjasto, ko. koodin käyttöön.
# Näin pystyt käyttämään haluttuja komentosanoja

# Datetime sisältää date objektin ja tällä on fuktio
# nimeltään today
today = datetime.date.today()
print(today.year, today.month, today.day)

# Jos tarvitset päivämäärän lisäksi kellonaikaa, niin
# silloin kannattaa käyttää datetime kirjaston sisältä
# datetime nimistä objektia ja sen now() funktiota
current_time = datetime.datetime.now()
print(current_time)

# Jos halutaan muokata tulostusinformaattia omanlaiseksi,
# niin voit käyttää strftime() nimistä funktiota
formatted_time = current_time.strftime("%d.%m.%y klo %H:%M")
# prosentti ja kirjain tarkoittaa, päivä, kuukausi, vuosi jne. %y on -25 ja %Y on 2025
print(formatted_time)



