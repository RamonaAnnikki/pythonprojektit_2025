# Kysytään käyttäjältä rahasumma sentteinä
rahasumma = int(input("Anna rahasumma (1-100 senttiä): "))

# Lista kolikoista suurimmasta pienimpään
kolikot = [50, 20, 10, 5, 2, 1]

# Sanakirja kolikoiden määreille
lukumaara = {}

# Lasketaan kolikoiden määrä
for kolikko in kolikot:
    lukumaara[kolikko] = rahasumma // kolikko # kuinka monta kolikkoa mahtuu
    rahasumma = rahasumma % kolikko           # jäljelle jäävä summa

# Tulostetaan tulos
print("Tarvittavat kolikot:")
for kolikko in kolikot:
    print(f"{kolikko} sentin kolikkoja: {lukumaara[kolikko]}")

