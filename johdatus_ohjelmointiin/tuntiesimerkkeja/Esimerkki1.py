print("Hello")
# Annetaan matka ja aika ja lasketaan nopeus
matka = 395.57 # Matka kilometreinä
aika = 5 # Aika tunteina

nopeus = round (matka / aika, 1)# Lasketaan tarkka arvo
#nopeus2 = round (nopeus, 2) # round funktio pyöristää luvun 2 desimaaliin
print(f"Matka oli {matka} km ja siinä kesti {aika} h. "
      f"Nopeutesi oli {nopeus} km/h")


