import os
import time

def clear_screen():
    _ = os.system('cls')

def animate():
    position = 0
    velocity = 1

    while True:
        clear_screen()

        position += velocity

        if position >= 10 or position <= 0:
            velocity = -velocity

        for i in range(10):
            if i == position:
                print("o", end="")
            else:
                print(" ", end="")
        print()

        time.sleep(0.1)

animate()