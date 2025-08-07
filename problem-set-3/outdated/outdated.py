months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ")
    if date[0].isdigit():
        listed = date.split("/")
        if "," in date:
            continue
        elif 0 < int(listed[0]) < 13 and 0 < int(listed[1]) < 32:
            print(listed[2] + "-", end="")
            print(listed[0].zfill(2) + "-", end="")
            print(listed[1].zfill(2))
            break
        else:
            continue
    elif date.split()[0] in months:
        if "," not in date:
            continue
        else:
            dated = date.replace(",", "")
            listed = dated.split()
            if 0 < int(listed[1]) < 32:
                print(listed[2] + "-", end="")
                print(str(months[listed[0]]).zfill(2) + "-", end="")
                print(listed[1].zfill(2))
                break
            else:
                continue



