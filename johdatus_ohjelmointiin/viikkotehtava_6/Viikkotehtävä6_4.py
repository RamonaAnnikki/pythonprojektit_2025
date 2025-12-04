# Lista tilauskoodeista
tilaukset = [
    "T1565_2020",
    "T2432_2019",
    "T8551_2018",
    "T3342_2019",
    "T9814_2018",
    "T7733_2020"
]

# Kysytään käyttäjältä vuosiluku
while True:
    try:
        vuosi = input("Anna vuosiluku (esim. 2019): ").strip()
        if len(vuosi) == 4 and vuosi.isdigit():
            break
        else:
            print("Anna nelinumeroinen vuosiluku.")
    except ValueError:
        print("Syötä numero, kiitos.")

print(f"\nTilauskoodit vuodelta {vuosi}:")

# Käydään lista läpi ja tulostetaan vain oikeat
loytyi = False
for t in tilaukset:
    koodi, tilausvuosi = t.split("_")  # erotetaan alaviivan kohdalta
    if tilausvuosi == vuosi:
        print(koodi)
        loytyi = True

if not loytyi:
    print("Ei tilauksia kyseiseltä vuodelta.")
