def slower():
    user_say = input()
    listed = list(user_say)
    counter = 0
    for i in range(len(listed)):
        if listed[i] == " ":
            listed[i] = "..."
            
    print("".join(listed))


slower()
