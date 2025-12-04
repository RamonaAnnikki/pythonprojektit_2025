# Peli on kivi-paperi-sakset
# Tehdään pelistä sellainen, että siinä pelataan konetta vastaan
#Tehdään sitten pelistä sellainen, että valinnat on numeroita, ja ne valitaan randomisti
#Eli otetaan käyttöön random -kirjasto
import random
kone = "paperi"
luku = random.randint(1, 3)
if luku == 1: kone = "kivi"
elif luku == 2: kone = "paperi"
elif luku == 3: kone = "sakset"
kayttaja = input("Valitse kivi, paperi tai sakset: ")

if (kone == "kivi" and kayttaja == "paperi") or\
    (kone == "paperi" and kayttaja == "sakset") or\
    (kone == "sakset" and kayttaja == "kivi"):
    print("Voitit")
elif kone == kayttaja:
    print("Tasapeli")
else:
    print("Hävisit")

print(f"Koneen valinta oli {kone}")


