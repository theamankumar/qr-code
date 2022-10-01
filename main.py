import pyqrcode
import png
from tkinter import *
from PIL import Image, ImageTk

def Generate():
    if my_entry.get():
        global qr_code,img
        qr_code = pyqrcode.create(my_entry.get())
        img = BitmapImage(data = qr_code.xbm(scale=8))
        img_lbl.config(image=img)    

root = Tk()
root.title('QR Code Generator')
root.geometry("500x500")

my_text=Label(root, text="Enter the Link:")
my_text.pack(pady=20)

my_entry=Entry(root)
my_entry.pack(pady=20)

my_button = Button(root,text="QR Code",command=Generate)
my_button.pack(pady=20)

qr_label=Label(root, text="Your QR Code")
qr_label.pack(pady=50)

img_lbl = Label(root)
img_lbl.pack()

root.mainloop()