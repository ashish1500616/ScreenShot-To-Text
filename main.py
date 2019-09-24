#! python3
import pyautogui, sys
import sys, termios, tty, os, time
import pytesseract
from PIL import Image
import pyperclip as pc
import keyboard
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.2
print('Press Ctrl-C to quit.')


try:
    a=0
    b=0
    c=0
    d=0
    while True:
        # char = getch()
        # if (char == "s"):
        if keyboard.is_pressed('s'):
            print("Stop!")
            exit(0)
        # elif (char == "a"):
        elif keyboard.is_pressed('a'):
            a, b = pyautogui.position()
            print("Top Co-ordinate to {} {} ".format(a,b))
        # elif(char == "b"):
        elif keyboard.is_pressed('b'):
            c, d = pyautogui.position()
            print("Bottom Co-ordinate to {} {} ".format(c,d))
        # elif (char == "p"):
        elif keyboard.is_pressed('p'):
            print("Top Co-ordinate {} {} ".format(a,b))
            print("Bottom Co-ordinate {} {} ".format(c,d))

        # elif (char == "c"):
        elif keyboard.is_pressed('c'):
            print("Bottom Co-ordinate {} {} {} {} ".format(a,b,c-a,d-b))
            im = pyautogui.screenshot(region=(a,b,c-a,d-b))
            txt=pytesseract.image_to_string(im)
            print("Processed txt\n {}".format(txt))
            pc.copy(txt)
            time.sleep(button_delay)


except KeyboardInterrupt:
    print('\n')