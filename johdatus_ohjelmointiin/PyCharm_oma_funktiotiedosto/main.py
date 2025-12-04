import functions

amount = float(input("Anna rahasumma: "))
from_currency = input("Anna valuutta (€, $, £, kr): ")
to_currency = input("Mihin valuuttaan muutetaan (€, $, £, kr): ")

result = functions.convert_money(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {result} {to_currency}")
