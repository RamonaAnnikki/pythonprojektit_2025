# Tuotelista
tuotteet = [ {"nimi": "omena", "hinta": 1.0},
    {"nimi": "banaani", "hinta": 1.2},
    {"nimi": "maito", "hinta": 2.0},
    {"nimi": "leipä", "hinta": 2.5} ]

ostoskori = []


def nayta_tuotteet():
    print("\nSaatavat tuotteet:")
    rivit = []
    for t in tuotteet:
        rivit.append(f"{t['nimi']} – {t['hinta']:.2f} €")
    print(" ".join(rivit))  # kaikki peräkkäin yhdellä rivillä
    print()


def lisaa_ostoskoriin():
    tuote_nimi = input("Anna tuotteen nimi: ").lower()
    for t in tuotteet:
        if t["nimi"] == tuote_nimi:
            ostoskori.append(t)
            print(f"{tuote_nimi} lisätty ostoskoriin.\n")
            return
    print("Tuotetta ei löytynyt!\n")


def nayta_ostoskori():
    if not ostoskori:
        print("\nOstoskori on tyhjä.\n")
        return

    print("\nOstoskorissa olevat tuotteet:")
    summa = 0
    for t in ostoskori:
        print(f"{t['nimi']} – {t['hinta']:.2f} €")
        summa += t["hinta"]

    print(f"\nLoppusumma: {summa:.2f} €\n")


# --- Pääohjelma ---
while True:
    print("1) Näytä saatavat tuotteet")
    print("2) Lisää tuote ostoskoriin")
    print("3) Näytä ostoskori ja loppusumma")
    print("4) Lopeta")

    valinta = input("Valitse (1-4): ")

    if valinta == "1":
        nayta_tuotteet()
    elif valinta == "2":
        lisaa_ostoskoriin()
    elif valinta == "3":
        nayta_ostoskori()
    elif valinta == "4":
        print("Ohjelma lopetetaan. Kiitos asioinnista ja mukavaa päivänjatkoa!")
        break
