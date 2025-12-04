# Kysytään kulutus
paiva_kwh = float(input("Paljonko sähköä kului päivällä (kWh)? "))
yo_kwh = float(input("Paljonko sähköä kului yöllä (kWh)? "))

# Kysytään hinnat senteissä
paiva_hinta = float(input("Päiväsähkön hinta (snt/kWh): "))
yo_hinta = float(input("Yösähkön hinta (snt/kWh): "))

# Lasketaan hinnat euroiksi
paiva_euro = paiva_kwh * (paiva_hinta / 100)
yo_euro = yo_kwh * (yo_hinta / 100)
yhteensa = paiva_euro + yo_euro

# Tulostetaan tulokset kahdella desimaalilla
print(f"Päiväsähkön hinta vuodessa: {paiva_euro:.2f} €")
print(f"Yösähkön hinta vuodessa: {yo_euro:.2f} €")
print(f"Yhteensä vuodessa: {yhteensa:.2f} €")
