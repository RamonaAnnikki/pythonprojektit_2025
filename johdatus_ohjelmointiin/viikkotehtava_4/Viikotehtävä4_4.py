try:
    # Pyydetään käyttäjältä kaksi lukua
    luku1 = float(input("Anna ensimmäinen numero: "))
    luku2 = float(input("Anna toinen numero: "))

    # Tarkistetaan nollalla jakaminen
    if luku2 == 0:
        print("Nollalla ei saa jakaa.")
    else:
        tulos = luku1 / luku2
        print(f"Jakolaskun tulos on: {tulos}")

# Jos käyttäjä syöttää jotain muuta kuin numeroita
except ValueError:
    print("Virheellinen muoto.")

