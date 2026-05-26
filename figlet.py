import sys
import pyfiglet
import random

fonts = pyfiglet.FigletFont.getFonts()
default_text = "Nu a huli ti loh"

if len(sys.argv) == 1:
    print(pyfiglet.figlet_format(default_text, font = random.choice(fonts)))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in fonts:
        text = input("Davai text: ")
        print(pyfiglet.figlet_format(text, font = sys.argv[2]))
    else:
        print("Net takogo shrifta dolboyob")

elif len(sys.argv) != 3 or sys.argv[1] == "-f" or sys.argv[1] == "--font":
    sys.exit()