

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two_letters(s) == True and how_long(s) == True and placing(s) == True and punctuation(s) == True:
        return True
    else:
        return False
def two_letters(word):
    if word[0:2].isalpha():
        return True
    else:
        return False

def how_long(lengthy):
    if 1 < len(lengthy) < 7:
        return True
    else:
        return False

def placing(where):
    numbers = []
    for i in where[2:len(where) - 1]:
        if i.isdigit():
            numbers.append(where[where.index(i):len(where) - 1])
            break

    if len(numbers) != 0:
        if numbers[0][0] != "0" and numbers[0].isdigit():
            return True
        else:
            return False
    else:
        return True

def punctuation(here):
    if '.' in here or ',' in here or '!' in here or ' ' in here:
        return False
    else:
        return True


main()
