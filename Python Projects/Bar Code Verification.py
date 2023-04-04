import cv2
from pyzbar.pyzbar import decode

#Reading QR Code from an Image
img = cv2.imread("qr2.png")
code = decode(img)

for barcode in decode(img):
    #print(barcode.data) #inbytes
    text = barcode.data.decode('utf-8')
    print(text)
    #print(barcode.rect)