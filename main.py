import pyautogui
import time
import numpy

pyautogui.PAUSE = 0.1


def GetPixelColor():    # Prints the color of the pixel being pointed at.
    x, y = pyautogui.position()
    pixel = pyautogui.screenshot().getpixel((x, y))
    
    print("Pixel color at position ({}, {}): {}".format(x, y, pixel))



color = (50, 72, 72)    # Color variables
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)

def ClickColor():   # Clicks a color specified by the "color" variable.
    ss = pyautogui.screenshot()

    for x in range(ss.width):
        for y in range(ss.height):
            if ss.getpixel((x, y)) == color:
                print(x, y)
                pyautogui.click(x, y)



def LocateAndClickTarget(): # Locates Elements matching with an image from the screen and clicks them.
    try:
        target = pyautogui.locateOnScreen('circle.png', confidence=0.9)
        if target is not None:
            #pyautogui.moveTo(target, _pause=False)
            pyautogui.click(target)
        else:
            print("Target not found. Retrying...")
    except Exception as e:
        print("Error.", e)
        print("Retrying...")



def Main(): # Choose which function to run
    while True:
        LocateAndClickTarget()  # Here

if __name__ == "__main__":
    Main()