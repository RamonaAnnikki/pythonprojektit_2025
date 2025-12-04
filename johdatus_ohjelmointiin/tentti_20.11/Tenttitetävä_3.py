def kerää_myynnit(oppilaat):
    myynnit = []
    for i in range(oppilaat):
        summa = float(input(f"Oppilaan {i+1} myynti (€): "))
        myynnit.append(summa)
    return myynnit

def laske_ja_tulosta(myynnit, menot):
    kokonaistulot = sum(myynnit)
    kokonaistuotto = kokonaistulot - menot
    keskiarvo = kokonaistuotto / len(myynnit)
    alle_kymmenen = sum(1 for x in myynnit if x < 10)

    print(f"\nKokonaistuotto menojen jälkeen: {kokonaistuotto:.2f} €")
    print(f"Keskimääräinen tuotto per oppilas: {keskiarvo:.2f} €")
    print(f"Alle 10 euroa myyneitä oppilaita: {alle_kymmenen}")

# --- Pääohjelma ---
oppilaita = int(input("Montako oppilasta luokalla on? "))
myynnit = kerää_myynnit(oppilaita)
menot = float(input("Kuinka paljon karkkipussien ostaminen maksoi yhteensä (€)? "))

laske_ja_tulosta(myynnit, menot)
