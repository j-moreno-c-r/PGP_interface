import tkinter as tk
from PIL import Image, ImageTk
import pyqrcode

def create_qr_code(input, text_subtitle, size=10 ):
        if isinstance(input, str):
                content = input
        else:
                with open(input, 'r') as file:
                        content = file.read()

        qr_code = pyqrcode.create(content)
        qr_code.png('qr_code.png', scale=size)

        window = tk.Tk()
        window.geometry('1000x1000')
        window.configure(bg='black')

        # Add a subtitle at the top of the window
        subtitle = tk.Label(window, text=text_subtitle, bg='black', fg='green', font=("Helvetica", 16))
        subtitle.pack()

        img = Image.open('qr_code.png')
        img = ImageTk.PhotoImage(img)

        label = tk.Label(window, image=img, bg='black')
        label.image = img
        label.pack()

        def increase_size():
                nonlocal size
                size += 1
                qr_code.png('qr_code.png', scale=size)
                img = Image.open('qr_code.png')
                img = ImageTk.PhotoImage(img)
                label.config(image=img)
                label.image = img

        # Increase button size
        button = tk.Button(window, text="Increase QR Code Size", command=increase_size, height=2, width=20, bg='green', fg='black')
        button.pack()

        # Close button
        close_button = tk.Button(window, text="Close", command=window.destroy, height=2, width=20, bg='green', fg='black')
        close_button.pack()

        # Bind Ctrl+W to close the window
        window.bind('<Control-w>', lambda event: window.destroy())

        window.mainloop()