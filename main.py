import pyqrcode
import png
link = input("Enter The Link: ")
qr_code = pyqrcode.create(link)
qr_code.png("code.png", scale=5)
