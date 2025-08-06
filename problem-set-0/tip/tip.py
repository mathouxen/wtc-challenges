def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_currency = d[1:len(d)]
    return float(no_currency)



def percent_to_float(p):
    no_unit = p[0:len(p) - 1]
    return float(int(no_unit) / 100)


main()
