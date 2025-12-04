# Lista tuotetunnisteista
tuotteet = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]

# Kategorioiden selitteet (0 = varalla jos numerointi alkaa 1:stä)
categories = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

# Käydään jokainen tuote silmukassa läpi
for tuote in tuotteet:
    osat = tuote.split("_")  # pilkotaan teksti alaviivojen kohdalta
    valmistaja = osat[0]
    nimi = osat[1]
    malli = osat[2]
    vuosi = osat[3]
    kuukausi = osat[4]
    paiva = osat[5]
    kategoria_numero = int(osat[-1])  # viimeinen arvo on numero 1–3
    kategoria = categories[kategoria_numero]

    print(f"Valmistaja: {valmistaja}")
    print(f"Nimi ja malli: {nimi} ({malli})")
    print(f"Kategoria: {kategoria}")
    print(f"Lisäyspäivämäärä: {int(paiva)}.{int(kuukausi)}.{vuosi}")
    print()  # tyhjä rivi väliin
