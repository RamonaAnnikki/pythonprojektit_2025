# Kysytään käyttäjältä lämpötila
lampotila = int(input("Anna kesäpäivän lämpötila: "))

# Tarkistetaan lämpötila ja tulostetaan vastaava teksti
if 0 <= lampotila <= 10:
    print("KYLMÄÄ")
elif 11 <= lampotila <= 15:
    print("KOLEAA")
elif 16 <= lampotila <= 20:
    print("MELKO LÄMMINTÄ")
elif 21 <= lampotila <= 25:
    print("LÄMMINTÄ")
elif 26 <= lampotila <= 30:
    print("HELLETTÄ")
else:
    print("Lämpötila ei kuulu määriteltyyn vaihteluväliin")
