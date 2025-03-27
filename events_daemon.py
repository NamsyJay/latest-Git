import threading 
import time


path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(5)
        
def printloop():
    for x in range(10):
        print(text)
        time.sleep(2)