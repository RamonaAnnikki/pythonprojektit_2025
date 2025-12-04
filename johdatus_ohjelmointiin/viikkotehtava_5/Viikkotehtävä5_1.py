# a) While-silmukka: luvut 1–50 allekkain
i = 1
while i <= 50:
    print(i)
    i += 1

# b) For-silmukka: luvut 1–50 allekkain
for i in range(1, 51):
    print(i)

# c) Summataan luvut 1–30
summa = 0
for i in range(1, 31):
    summa += i
print("Summa väliltä 1–30 on:", summa)

# d) Tulostetaan vuosiluvut 2005–2010 yhdelle riville
for vuosi in range(2005, 2011):
    print(vuosi, end=" ")
