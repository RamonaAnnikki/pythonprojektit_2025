# Tehdään tuple, jossa on kuukaudet
kuukaudet = (
    "Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu",
    "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu",
    "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"
)

# Kysytään käyttäjältä kuukauden numero
while True:
    try:
        numero = int(input("Anna kuukauden numero (1–12): "))
        if 1 <= numero <= 12:
            print(f"{numero}. kuukausi on {kuukaudet[numero - 1]}.")
            break
        else:
            print("Anna numero väliltä 1–12.")
    except ValueError:
        print("Syötä kokonaisluku, kiitos.")
