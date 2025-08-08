import pyfiglet
import sys
fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    plain = input("Input: ")
    print(pyfiglet.figlet_format(plain))
elif len(sys.argv) == 3:
    if sys.argv[2] not in fonts:
        sys.exit("Font not available")
    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
        plain = input("Input: ")
        print(pyfiglet.figlet_format(plain, font=sys.argv[2]))
    else:
        sys.exit("Font not available")
else:
    sys.exit("Font not available")
