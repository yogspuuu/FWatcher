import time
import string
import random

def loop(file):
    with open(file, "w", encoding="utf-8") as file:
        file.write(random.choice(string.ascii_letters))

if __name__ == '__main__':
    while True:
        loop("/home/yoga/Codingan/Project/FWatcher/test/log.txt")
        time.sleep(5)
