import pyqrcode
import tkinter as tk

def create_qr_code(key,subtitle, size=5,v=40):
        qr_code = pyqrcode.create(key, error='L', version=v)
        qr_code_xbm = qr_code.xbm(scale=size)
        top = tk.Toplevel()
        subtitle = tk.Label(top, text=subtitle)  # Create a new label with the subtitle
        subtitle.pack()  # Pack the subtitle label before the QR code
        code_bmp = tk.BitmapImage(data=qr_code_xbm)
        code_bmp.config(background="white")
        label = tk.Label(top, image=code_bmp)
        label.image = code_bmp  # Keep a reference to the image object
        label.pack()
        return top

