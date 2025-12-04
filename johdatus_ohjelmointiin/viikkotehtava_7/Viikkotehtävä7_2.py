# Kolme erillistä listaa
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

# Yhdistetään listat suurempaan listaan
inventory = [fruits, berries, vegetables]

# Tulostetaan kaikki sisällöt kahdella silmukalla
for category in inventory:          # käy läpi jokaisen alilistan
    for item in category:           # käy läpi yksittäiset sanat alilistassa
        print(item)
