# Lista, joka sisältää sanakirjoja (dictionary)
movies = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Tuntematon sotilas", "year": 1955},
    {"name": "Leijonasydän", "year": 2013},
    {"name": "Napapiirin sankarit", "year": 2010}
]

# Tyhjät listat eri aikakausille
old_movies = []
new_movies = []

# Käydään läpi elokuvat ja jaotellaan ne
for movie in movies:
    if movie["year"] < 2000:
        old_movies.append(movie["name"])
    else:
        new_movies.append(movie["name"])

# Värit PyCharmin konsoliin
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Tulostetaan tulokset
print(f"{CYAN}2000-luvun elokuvat:{RESET}")
for movie in new_movies:
    print("-", movie)

print()
print(f"{GREEN}Vanhemmat elokuvat:{RESET}")
for movie in old_movies:
    print("-", movie)

