import keyboard
import mouse
import time
import sys


def main():
    speed = sys.argv[1]
    total_count = sys.argv[2]

    while True:
        key = keyboard.read_key()
        if key == "esc":
            break

        if key == "c":
            is_clicking = True
            click_count = 0
            while is_clicking:
                mouse.click("left")
                print("left button was clicked")
                click_count += 1
                time.sleep(float(speed))
                print(click_count)
                if click_count > int(total_count):
                    is_clicking = False


main()
