# Python
Qr-Code
First "pip install pyqrcode" 
      run "python Qr-Code.py"
      input the ur url

Code is =

import pyqrcode

from pyqrcode import QRCode

#write ur url and enter

s = input("url: ")

url = pyqrcode.create(s)

url.svg("qrcode.svg", scale = 8)
