# importataan kirjasto math, tällaiseen koodiin on oma kaava!
# (siitä tulee nuo kirjaimet muuttujiksi)!!
# A=P.(1+r)potenssiin-t
# P=alkupääoma, r=korko (desimaalina), t=vuosien päästä
import math

P = float(input("Anna alkupääoma: "))
r = float(input("Anna korkoprosentti: "))
t = float(input("Montako vuotta pääomaa voidaan tallentaa: "))
# Tässä annetaan kirjainten/muuttujien toiminto ja mitä niiden halutaan "sanovan"!
# Itse arvot syötetään sitten vasta "päällä olevaan" ohjelmaan!!

A = P * math.pow(1+r, t)

print(f"Pääomasi {t} vuoden kuluttua on {round(A, 2)} €")



