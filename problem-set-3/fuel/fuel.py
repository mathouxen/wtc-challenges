import operator


while True:
    division = operator.truediv
    fraction = input("Fraction: ")
    listed = fraction.split("/")
    if len(fraction.split("/")) == 2:
        if listed[0].isdigit() and listed[1].isdigit():
            try:
                percentage = 100 * division(int(listed[0]), int(listed[1]))
                p_str = str(percentage)
            except ZeroDivisionError:
                pass
            else:
                if percentage <= 1:
                    print("E")
                    break
                elif percentage >= 99:
                    print("F")
                    break
                elif int(p_str[3]) > 4:
                    display = str(percentage + 1)
                    print(f"{display[0:2]}%")
                    break
                else:
                    print(f"{p_str[0:2]}%")
                    break

    else:
        continue
