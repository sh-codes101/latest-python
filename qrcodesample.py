#make sure to download pillow and q code library ny doing pip install pillow , pip install qrcode

import qrcode #import qr code lib

data = 'https://www.youtube.com/channel/UCUzkbteGeoDpiP3ntsgE7IQ' #the data to be shown when using qr

qr = qrcode.make(data) #makes qr code

qr.save('qrcode.png') # saves qr code

print('qr code generated and saved succesfully .') #print statement 