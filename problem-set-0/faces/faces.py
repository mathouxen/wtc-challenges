def emoji():
    plain = input("")
    animated = []
    counter = 0


    while counter < len(plain):
        if plain[counter:counter + 2] == ":)":
            animated.append("🙂")
            counter = counter + 2
        elif plain[counter:counter + 2] == ":(":
            animated.append("🙁")
            counter = counter + 2
        else:
            animated.append(plain[counter])
            counter = counter + 1

    print("".join(animated))

emoji()
