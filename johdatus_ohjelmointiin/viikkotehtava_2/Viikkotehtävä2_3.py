print("Käteen jäävän palkan laskenta")

# Kysy käyttäjältä kuukausipalkka ja veroprosentti
palkka = float(input("Anna kuukausipalkka (€): "))
vero_prosentti = float(input("Anna veroprosentti (%): "))

# Laske vero ja käteen jäävä osuus
vero = palkka * vero_prosentti / 100
kateen = palkka - vero

# Tulosta tulokset
print(f"Verot: {vero:.2f} €")
print(f"Käteen jäävä palkka: {kateen:.2f} €")