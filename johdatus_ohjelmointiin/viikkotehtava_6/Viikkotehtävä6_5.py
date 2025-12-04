# a) Luodaan lista
basket = ["omena", "banaani", "kirsikka", "porkkana", "peruna", "tomaatti", "kaali"]

# b) Etsitään sana listasta
hakusana = input("Anna etsittävä sana: ").lower()

for sana in basket:
    if sana == hakusana:
        print("Sana löytyi!")
        break
    else:
        print("Etsitään…")
else:
    # Tämä else kuuluu for-silmukalle: suoritetaan vain jos break ei katkaissut silmukkaa
    print("Sanaa ei löytynyt listasta.")

print()  # tyhjä rivi väliin

# c) Kysy sana tai numero
valinta = input("Anna sana tai numero: ")

print("\nBasket-listan sisältö:")

# Jos käyttäjä syötti numeron
if valinta.isnumeric():
    indeksi = int(valinta)
    for i in range(len(basket)):
        if i == indeksi:
            continue  # ohitetaan tämä alkio
        print(basket[i])

# Jos käyttäjä syötti sanan
else:
    for sana in basket:
        if sana == valinta.lower():
            continue  # ohitetaan tämä sana
        print(sana)
