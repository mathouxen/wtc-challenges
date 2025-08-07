def snaking():
    camel_case = input("camelCase: ")
    listed = []

    for i in camel_case:
        if i.isupper():
            listed.append("_" + i.lower())
        else:
            listed.append(i)


    print("".join(listed))


snaking()
