# Simple checks using clean and readable code

def check_value_greater_than_ten(value):
    """
    Checks whether the given value is greater than 10.
    Prints 'OK' if true, otherwise 'NO'.
    """
    if value > 10:
        print("OK")
    else:
        print("NO")


def check_double_value_level(number):
    """
    Doubles the given number.
    Prints 'LOW' if the doubled value is less than 20,
    otherwise prints 'HIGH'.
    """
    doubled_value = number * 2

    if doubled_value < 20:
        print("LOW")
    else:
        print("HIGH")


# ---- Main program ----

check_value_greater_than_ten(5)
check_double_value_level(15)
