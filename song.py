import time
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

#print(Fore.MAGENTA + Style.BRIGHT + "🎶 Now Playing: Tujhe Keh Doon Ya Rehne Doon 🎶\n")
#time.sleep(2.5)

# (color, line)
lyrics = [
    (Fore.RED,    "❤️ Tujhe keh doon ya rehne doon raaz mere..."),
    (Fore.CYAN,   "💭 Sab kuch keh doon kya tujhko?"),
    (Fore.YELLOW, "😔 Tu mujhko chhod jaayegi ya aayegi paas mere..."),
    (Fore.BLUE,   "🌧️ Isi baat ka darr hai mujhko..."),
    ("",           ""),
    (Fore.RED,    "💘 Ke ho na jaaye pyaar tumse mujhe..."),
    (Fore.MAGENTA,"💔 Kar dega barbaad ishq mujhe..."),
    (Fore.RED,    "❤️ Ho na jaaye pyaar tumse mujhe...")
]

def type_line(color, text, speed=0.05):
    """Typewriter effect function"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # next line
    time.sleep(1.5)

for color, line in lyrics:
    type_line(color, line)

print(Style.BRIGHT + Fore.GREEN + "\n")
