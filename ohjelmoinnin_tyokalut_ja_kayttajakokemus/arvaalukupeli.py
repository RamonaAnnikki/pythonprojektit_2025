import random

def arvaa_luku():
    # Satunnainen luku 1–10
    salainen_luku = random.randint(1, 10)

    # Yritysten laskuri
    yritykset = 0

    # Alustetaan arvaus
    arvaus = None

    print("Tervetuloa arvauspeliin!")
    print("Arvaa luku väliltä 1–10.")

    # Peli jatkuu kunnes arvaus == salainen_luku
    while arvaus != salainen_luku:
        arvaus = int(input("Anna arvauksesi: "))

        # Jokaisella kierroksella yritykset +1
        yritykset += 1

        # Annetaan vihje
        if arvaus < salainen_luku:
            print("Liian pieni!")
        elif arvaus > salainen_luku:
            print("Liian suuri!")
        else:
            # Oikea arvaus
            print(f"Oikein! Arvasit luvun {salainen_luku} oikein {yritykset} yrityksellä.")

arvaa_luku()
