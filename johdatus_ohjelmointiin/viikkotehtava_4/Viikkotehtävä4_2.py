# Kysytään käyttäjältä teksti
teksti = input("Anna teksti: ")

# Tarkistetaan, onko syöte tyhjä
if teksti == "":
    print("Antamasi teksti on tyhjä.")
else:
    # Käännetään teksti toisinpäin
    kaannetty = teksti[::-1]
    print(f"Käännettynä: {kaannetty}")

    # Tarkistetaan, onko teksti palindromi
    if teksti == kaannetty:
        print("KYLLÄ, teksti on palindromi.")
    else:
        print("EI, teksti ei ole palindromi.")
