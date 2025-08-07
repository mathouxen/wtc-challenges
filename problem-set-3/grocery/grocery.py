
itinerary = []
final = []


while True:
    try:
        item = input("")
        itinerary.append(item)
    except EOFError:
        for i in itinerary:
            how_many = itinerary.count(i)
            final.append((str(how_many) + " " + i.upper()))
        dopple = set(final)
        print()
        for item in dopple:
            print(item)
        break
