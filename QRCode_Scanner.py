import cv2
from imutils.video import VideoStream
from pyzbar import pyzbar
from time import sleep
import imutils
import time
import os,sys
import webbrowser

print("[info] Scanning.....")
v = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = v.read()
    frame = imutils.resize(frame,width=1000)
    qrcode = pyzbar.decode(frame)

    for qrcodes in qrcode:
        (x,y,w,h) = qrcodes.rect
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,0,255) , 2)

        qrcode_data = qrcodes.data.decode("utf-8") # for converting img to str
        qrcode_type = qrcodes.type 

        text = '{} '.format(qrcode_data)
        cv2.putText(frame , text , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,255) , 2)
        print(text)

        url = text
        webbrowser.open_new_tab(url)

    cv2.imshow("QRcode Scanner",frame)
    key = cv2.waitKey(1) & 0xFF

    if key==ord('q'):
        break
        
cv2.destroyAllWindows()
