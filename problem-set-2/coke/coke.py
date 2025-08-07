def coke():

    amount_due = 50

    while amount_due > 0:
        
        print(f"Amount due: {amount_due}")
        coin = input("Insert coin: ")
        if coin == "25" or coin == "10" or coin == "5":
            amount_due = amount_due - int(coin)


    if amount_due == 0:
        print(f"Amount due: {amount_due}")
        print(f"Change owed: {amount_due}")
    elif amount_due < 0:
        change = amount_due * -1
        print(f"Amount due: 0")
        print(f"Change owed: {change}")

coke()
