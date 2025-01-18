import pyqrcode
import png
from pyqrcode import QRCode

address = "https://chitanka.info/"

url = pyqrcode.create(address)
url.png("test.png", scale=8)