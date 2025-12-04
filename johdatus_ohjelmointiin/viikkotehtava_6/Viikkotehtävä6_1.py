# Pyydetään käyttäjältä 5 positiivista kokonaislukua ja etsitään suurin

suurin = 0  # apumuuttuja suurimman luvun tallentamiseen

for i in range(5):
    while True:
        try:
            luku = int(input(f"Anna positiivinen luku ({i+1}/5): "))
            if luku > 0:
                break
            else:
                print("Luvun täytyy olla positiivinen.")
        except ValueError:
            print("Anna kokonaisluku, kiitos!")

    # Päivitetään suurin tarvittaessa
    if luku > suurin:
        suurin = luku

print(f"Suurin antamasi luku on {suurin}.")
