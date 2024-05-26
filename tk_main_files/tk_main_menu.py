import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from .tk_qr_menu import create_qr_interface
from .tk_register_keys import register_keys
from .tk_main_decry_encry import main_window

def create_main_menu():
    global root
    root = ThemedTk(theme="clearlooks")
    root.configure(bg='black')
    root.title("Main Menu")

    # Add background image
    image = Image.open("main_bg.jpeg")
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.geometry("%dx%d" % (image.width, image.height))

    button1 = tk.Button(root, text="Register Keys", command=lambda: register_keys(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button1.place(x=20, y=20)  

    button2 = tk.Button(root, text="Decrypt and Encrypt", command=lambda: main_window(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button2.place(x=20, y=60) 

    button3 = tk.Button(root, text="QR Keys", command=lambda: create_qr_interface(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button3.place(x=20, y=100) 

    tutorial_text = "Wake Up, Neo...\n The Matrix has you...\n Follow the white rabbit...\n Knock, knock, Neo." 
    tutorial_label = tk.Label(root, text=tutorial_text, bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=5, relief="groove")
    tutorial_label.place(x=20, y=140)  

    # Bind Ctrl+W to close the window
    root.bind('<Control-w>', lambda event: root.destroy())

    root.mainloop()