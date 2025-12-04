import random

# Värikoodit
CYAN = "\033[96m"
RESET = "\033[0m"

# Lue mietelauseet
with open("wisewords.txt", "r", encoding="utf-8") as file:
    wise_list = [line.strip() for line in file]

max_index = len(wise_list) - 1
random_index = random.randint(0, max_index)

# Tulostus
print("Tämän päivän mietelause:")
print(CYAN + wise_list[random_index] + RESET)
