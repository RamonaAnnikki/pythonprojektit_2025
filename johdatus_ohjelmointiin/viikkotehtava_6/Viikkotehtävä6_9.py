# Sanakirja, joka yhdistää numeron ja sen sanan
numerot_sanoina = {
    "0": "nolla",
    "1": "yksi",
    "2": "kaksi",
    "3": "kolme",
    "4": "neljä",
    "5": "viisi",
    "6": "kuusi",
    "7": "seitsemän",
    "8": "kahdeksan",
    "9": "yhdeksän"
}

while True:
    numero = input("Anna luku (enintään 5 numeroa): ").strip()

    # Tarkistetaan, että syöte on numeerinen ja enintään 5 merkkiä
    if numero.isdigit() and len(numero) <= 5:
        break
    else:
        print("Virheellinen syöte! Anna vain numeroita, korkeintaan 5 merkkiä.")

# Muutetaan numerot sanoiksi
sanat = [numerot_sanoina[n] for n in numero]

# Tulostetaan välilyönneillä erotettuna
print(" ".join(sanat))
