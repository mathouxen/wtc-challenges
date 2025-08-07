



menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def order():
    total = 0
    try:
        while True:
            item = input("Item: ")
            if item.title() in menu:
                total = total + menu[item.title()]
                press = format(total, ".2f")
                print(f"Total: ${press}")
    except EOFError:
        print()
        return

order()
 