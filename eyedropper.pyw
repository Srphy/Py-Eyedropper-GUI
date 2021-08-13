import cv2
import numpy as np
import pyautogui as pg
import colorutils
import pyperclip

def capture():
    global output, bgr2, output

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

def clip():
    pyperclip.copy(output)
    print("colors copied to clipboard :", output)

size = 50
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 45)
org2 = (10, 490)
org3 = (25, 95)
fontScale = 0.95
fontScale2 = 0.5
fontScale3 = 0.75
fontColor = (184, 191, 194) # bgr non rgb values
thickness = 1

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
    tx1 = cv2.putText(im, 'S to copy, Esc to shut down', org, font, fontScale, fontColor, thickness, cv2.LINE_AA)
    tx2 = cv2.putText(im, output, org3, font, fontScale3, fontColor, thickness, cv2.LINE_AA)
    check = cv2.rectangle(im,(200,405),(300,305),bgr2, -1)
    contour = cv2.rectangle(im,(200,405),(300,305),(60, 60, 60), 2)
    bottomBorder = cv2.rectangle(im,(0,500),(500,469),(60, 60, 60), -1)
    bottomContour = cv2.rectangle(im,(-3,500),(503,469),(0, 0, 0), 1)
    tx3 = cv2.putText(im, posxy, org2, font, fontScale2, fontColor, thickness, cv2.LINE_AA)
    fullBorder = cv2.rectangle(im,(0,0),(499,499),(0, 0, 0), 1)  

    im = cv2.rectangle(im, (st, st), (ed, ed), (0, 0, 0), 2)

    cv2.imshow("Color Picker", im,)    
    capture()
    
    k = cv2.waitKey(1)
    if k==115: # Lowercase S to save color output                
        clip()
    if k==27: # Esc key to breakloop and shutdown
        break

cv2.destroyAllWindows()