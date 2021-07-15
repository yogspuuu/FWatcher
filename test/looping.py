import time
import string
import random

def loop(file):
    letters = string.ascii_letters
    with open(file, "w", encoding="utf-8") as file:
        file.write(random.choice(letters))

if __name__ == '__main__':
    while True:
        loop("/home/yoga/Codingan/Project/FWatcher/test/log.txt")
        time.sleep(5)
