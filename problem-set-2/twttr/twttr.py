def main():
    fully = input("Input: ")
    print(shorten(fully))


def shorten(word):
    contracted = []
    for alpha in word:
        if alpha.lower() == "a" or alpha.lower() == "e" or alpha.lower() == "o" or alpha.lower() == "i" or alpha.lower() == "u":
            continue
        else:
            contracted.append(alpha)

    return f"{''.join(contracted)}"



if __name__ == "__main__":
    main()
