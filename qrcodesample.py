#make sure to download pillow and qrcode library by doing pip install pillow , pip install qrcode

import qrcode #import qr code lib

data = '' #the data to be shown when using qr

qr = qrcode.make(data) #makes qr code

qr.save('qrcode.png') # saves qr code

print('qr code generated and saved succesfully .') #print statement 
