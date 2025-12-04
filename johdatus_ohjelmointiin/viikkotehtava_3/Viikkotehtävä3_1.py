# Kysytään käyttäjältä kaksi kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))

# Verrataan lukuja
if luku1 > luku2:
    print("Suurempi luku on:", luku1)
elif luku2 > luku1:
    print("Suurempi luku on:", luku2)
else:
    print("Numerot ovat yhtä suuria.")
