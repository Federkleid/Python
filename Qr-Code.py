import pyqrcode
from pyqrcode import QRCode
#write ur url and enter
s = input("url: ")

url = pyqrcode.create(s)

url.svg("qrcode.svg", scale = 8)
