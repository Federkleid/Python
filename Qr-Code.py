import pyqrcode
from pyqrcode import QRCode

s = input("url: ")

url = pyqrcode.create(s)

url.svg("qrcode.svg", scale = 8)
