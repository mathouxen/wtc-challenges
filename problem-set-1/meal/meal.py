__name__ = "__main__"

def main():
    what_the_time = input("What time is it? ")


    convert(what_the_time)


    if 7 <= convert(what_the_time) <= 8:
        print("breakfast time")
    elif 12 <= convert(what_the_time) <= 13:
        print("lunch time")
    elif 18 <= convert(what_the_time) <= 19:
        print("dinner time")
    else:
        print("")




def convert(time):
    minutes = int(time[len(time) - 2:len(time)])
    decimal = minutes / 60

    if len(time) == 4:
        return int(time[0:1]) + decimal
    else:
        return int(time[0:2]) + decimal

if __name__ == "__main__":
    main()
