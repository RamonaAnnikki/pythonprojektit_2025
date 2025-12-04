import math  # saadaan π (pi) käyttöön

while True:
    try:
        sade = float(input("Anna ympyrän säde (cm): "))
        if sade < 0:
            print("Säde ei voi olla negatiivinen.")
            continue
        pinta_ala = math.pi * (sade ** 2)
        print(f"Ympyrän pinta-ala on {pinta_ala:.2f} cm².")
    except ValueError:
        print("Anna numero, kiitos.")
        continue

    jatka = input("Haluatko jatkaa? (k/e): ").lower()
    if jatka == "e":
        print("Ohjelma lopetetaan.")
        break
