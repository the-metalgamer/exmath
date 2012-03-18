import decimal

def cube_root(number):
    decimal.getcontext().prec = 16
    a = decimal.Decimal(number)
    current_value = decimal.Decimal(number) / (decimal.Decimal(3) ** 2)
    if current_value <= decimal.Decimal("1.0"):
        current_value = decimal.Decimal("1.1")
        last_value = 0
        while last_value != current_value:
            last_value = current_value
            current_value = (1 / decimal.Decimal(3)) * (((decimal.Decimal(2)) *
                        current_value) + (a / (current_value **
                            decimal.Decimal(2))))
    return float(current_value)
