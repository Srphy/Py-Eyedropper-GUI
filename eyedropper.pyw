import cv2
import numpy as np
import pyautogui as pg
import colorutils
import pyperclip

size = 50

def capture():
    global output, bgr2, output, color, hex

    pos = pg.position()
    s = pg.screenshot(region=(pos[0] - 1, pos[1] - 1, 1, 1))
    s = np.array(s)

    s2 = np.flip(s, axis=None) # Array color inversion for screen display
    result2 = tuple(s2[0, 0]) # Float bgr value
    hex2 = colorutils.rgb_to_hex(result2) # Convert hex value
    bgr2 = colorutils.hex_to_rgb(hex2) # Final bgr value
    
    result = tuple(s[0, 0]) # Float rgb values    
    color = str(result) # Screen rgb result
    hex = colorutils.rgb_to_hex(result) # Screen hex values     
    output = color + " - " + hex # Final rgb & hex values
    
capture()

def clip1():
    pyperclip.copy(output)
    print("colors copied to clipboard :", output)
def clip2():
    pyperclip.copy(color)
    print("colors copied to clipboard :", color)
def clip3():
    pyperclip.copy(hex)
    print("colors copied to clipboard :", hex)

while True:
    pos = pg.position()
    posxy = str(pos)
    s = pg.screenshot(region=(pos[0] - size/2, pos[1] - size/2, size, size))

    im = cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR) # Color space inversion 
    im = cv2.resize(im, (size*10, size*10), interpolation=cv2.INTER_AREA)

    st = int((size*10)/2 - 5)
    ed = int((size*10)/2 + 5)
    
    topBorder = cv2.rectangle(im,(0,0),(500,115),(60, 60, 60), -1)
    topContour = cv2.rectangle(im,(-3,0),(503,115),(0, 0, 0), 1)
    tx1 = cv2.putText(im, 'Q to copy rgb value, S to copy hex value', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (184, 191, 194), 1, cv2.LINE_AA)
    tx1_2 = cv2.putText(im, 'D to copy both, Esc to shut down', (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (184, 191, 194), 1, cv2.LINE_AA)
    tx2 = cv2.putText(im, output, (25, 95), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (184, 191, 194), 1, cv2.LINE_AA)
    check = cv2.rectangle(im,(200,405),(300,305),bgr2, -1)
    contour = cv2.rectangle(im,(200,405),(300,305),(60, 60, 60), 2)
    bottomBorder = cv2.rectangle(im,(0,500),(500,469),(60, 60, 60), -1)
    bottomContour = cv2.rectangle(im,(-3,500),(503,469),(0, 0, 0), 1)
    tx3 = cv2.putText(im, posxy, (10, 490), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (184, 191, 194), 1, cv2.LINE_AA)
    fullBorder = cv2.rectangle(im,(0,0),(499,499),(0, 0, 0), 1)  

    im = cv2.rectangle(im, (st, st), (ed, ed), (0, 0, 0), 2)

    cv2.imshow("Color Picker", im,)    
    capture()
    
    k = cv2.waitKey(1)

    if k==113: # Lowercase Q to save rgb output
        clip2()
    if k==115: # Lowercase S to save hex output
        clip3()
    if k==100: # Lowercase D to save both color outputs
        clip1()
    if k==27: # Esc key to breakloop and shutdown
        break

cv2.destroyAllWindows()