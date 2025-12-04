
import random

def arvaa_luku():
    salainen_luku = random.randint(1, 10)
    yritykset = 0
    arvaus = None

    print("Tervetuloa arvauspeliin!")
    print("Arvaa luku väliltä 1–10.")

    while arvaus != salainen_luku:
        arvaus = int(input("Anna arvauksesi: "))
        yritykset += 1

        if arvaus < salainen_luku:
            print("Liian pieni!")
        elif arvaus > salainen_luku:
            print("Liian suuri!")
        else:
            print(f"Oikein! Arvasit luvun {salainen_luku} oikein {yritykset} yrityksellä.")

arvaa_luku()
