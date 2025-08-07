def calories():
    fruit = input("Item: ").lower()

    fifty = ["tangerine", "strawberries", "pineapple", "honeydew melon", "cantaloupe", "avocado"]
    sixty = ["grapefruit", "nectarine", "peach"]
    eighty = ["watermelon", "orange"]
    ninety = ["kiwifruit", "grapes"]
    hundred = ["sweet cherries", "pear"]

    if fruit == "lemon":
        print("Calories: 15")
    elif fruit == "lime":
        print("Calories: 20")
    elif fruit in fifty:
        print("Calories: 50")
    elif fruit in sixty:
        print("Calories: 60")
    elif fruit == "plums":
        print("Calories: 70")
    elif fruit in eighty:
        print("Calories: 80")
    elif fruit in ninety:
        print("Calories: 90")
    elif fruit in hundred:
        print("Calories: 100")
    elif fruit == "banana":
        print("Calories: 110")
    elif fruit == "apple":
        print("Calories: 130")
    else:
        print(end="")

calories()
