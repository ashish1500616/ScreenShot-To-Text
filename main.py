#! python3
import pyautogui, sys
import pytesseract
from PIL import Image
import pyperclip as pc
import keyboard
 


try:
    a=0
    b=0
    print("Script Started...................................................")
    print("Press a or 1 to catch the top co-ordinate of a part of a screen.")
    print("Press c or 2 to catch the bottom co-ordinate and to extract text.")
    print("Press 'S'  to stop the script.")

    while True:
        if keyboard.is_pressed('S'):
            print("Stop!...................................................")
            exit(0)
        elif keyboard.is_pressed('a') or keyboard.is_pressed('1') :
            a, b = pyautogui.position()
            print("Top Co-ordinate {} {} ".format(a,b))
        elif keyboard.is_pressed('p'):
            print("Top Co-ordinate {} {} ".format(a,b))
            print("Bottom Co-ordinate {} {} ".format(c,d))

        elif keyboard.is_pressed('z') or keyboard.is_pressed('2') :
            c, d = pyautogui.position()
            print("\nBottom Co-ordinate to {} {} ".format(c,d))
            # print("Top Width Height {} {} {} {} ".format(a,b,c-a,d-b))
            im = pyautogui.screenshot(region=(a,b,c-a,d-b))
            txt=pytesseract.image_to_string(im)
            pc.copy(txt)

except KeyboardInterrupt:
    print('\n')
    
# except:
#     print("Something else went wrong")