import random

print("Tervetuloa venttipeliin!\n")

# Pelaajan alku
pelaajan_summa = random.randint(1, 13)
print(f"Sait kortin: {pelaajan_summa}")

# Pelaajan vuoro
while True:
    vastaus = input("Haluatko uuden kortin? (k/e): ").lower()

    if vastaus == "k":
        uusi = random.randint(1, 13)
        pelaajan_summa += uusi
        print(f"Sait kortin: {uusi} (summa nyt {pelaajan_summa})")

        if pelaajan_summa > 21:
            print("Yli 21! Hävisit pelin.")
            exit()

    else:
        break

# Koneen vuoro (vain jos pelaaja ei mennyt yli)
print("\nKone arpoo nyt omat korttinsa...")

kone_summa = 0
for i in range(3):
    kortti = random.randint(1, 13)
    kone_summa += kortti
    print(f"Koneen kortti {i+1}: {kortti}")

print(f"\nKoneen summa: {kone_summa}")
print(f"Pelaajan summa: {pelaajan_summa}\n")

# Voittajan määritys
if kone_summa > 21:
    print("Kone meni yli 21 → pelaaja voittaa!")
elif kone_summa > pelaajan_summa:
    print("Kone voittaa!")
else:
    print("Pelaaja voittaa!")
