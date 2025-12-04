import math

def laske_hinta(tyyppi, paino):
    if tyyppi == "kirje":
        perushinta = 0.50
        if paino < 200:
            return perushinta
        elif paino <= 500:
            lisamaksu = math.floor((paino - 200) / 100) * 0.04
            return perushinta + lisamaksu
        else:
            lisamaksu = math.floor((paino - 200) / 100) * 0.04
            hinta = perushinta + lisamaksu
            postilaatikko = input("Mahtuuko kirje postilaatikkoon? (kyllä/ei): ").lower()
            if postilaatikko == "ei":
                hinta += 2.00
            return hinta

    elif tyyppi == "paketti":
        perushinta = 2.00
        if paino < 200:
            return perushinta
        elif paino <= 500:
            lisamaksu = math.floor((paino - 200) / 100) * 0.08
        else:
            lisamaksu = math.floor((paino - 200) / 100) * 0.14
        return perushinta + lisamaksu

    else:
        return None


# !!Pääohjelma alkaa tästä!!
tyyppi = input("Anna lähetystyyppi (kirje/paketti): ").lower()
paino = int(input("Anna lähetyksen paino grammoina: "))

hinta = laske_hinta(tyyppi, paino)

if hinta is None:
    print("Virhe: tuntematon lähetystyyppi.")
else:
    print(f"Lähetyksen hinta on: {hinta:.2f} €")
