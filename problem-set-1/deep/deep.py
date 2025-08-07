def universe():
    ask = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if ask == "42" or ask == "forty-two" or ask == "forty two":
        print("Yes")
    else:
        print("No")



universe()
