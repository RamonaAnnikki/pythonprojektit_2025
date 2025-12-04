# Kertotauluohjelma, joka tulostaa lukujen 1–10 kertotaulut
# ja lopettaa, jos käyttäjä syöttää 0

while True:
    try:
        luku = int(input("Anna luku väliltä 1–10 (tai 0 lopettaaksesi): "))

        if luku == 0:
            print("Ohjelma lopetetaan.")
            break  # poistutaan silmukasta kokonaan

        if 1 <= luku <= 10:
            print(f"\nKertotaulu luvulle {luku}:")
            for i in range(1, 11):
                print(f"{luku} x {i} = {luku * i}")
            print()  # tyhjä rivi väliin
        else:
            print("Virhe: anna luku väliltä 1–10.")

    except ValueError:
        print("Anna kokonaisluku, kiitos.")

