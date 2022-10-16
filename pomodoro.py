# CLI app that takes in 3 numbers for length, short break time, and long break time, and alerts when time ends
import time

rounds = 0

length = int(input("Study Length (minutes): ")) * 60
sbreak = int(input("Short Break Length (minutes): ")) * 60
lbreak = int(input("Long Break Length (minutes): ")) * 60
max_rounds = int(input("How many sessions before Long Break: "))

while True:
    if rounds < max_rounds:
        input(f"Start study time? (ENTER)")
        time.sleep(length)
        rounds += 1
        if rounds < max_rounds:          
            input(f"Start break time? (ENTER)")
            time.sleep(sbreak)
        
    else:
        input("Start Long Break? (ENTER)")
        time.sleep(lbreak)
        rounds = 0


