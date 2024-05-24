import tkinter as tk
from tk_encrypt_decrypt import create_tk_interface
from tk_qr_menu import create_qr_interface
from tk_register_keys import register_keys
def show_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.configure(bg='black')
    tk.Label(new_window, text=f"This is the {title} window", bg='black', fg='#98FB98').pack()

def create_main_menu():
    global root
    root = tk.Tk()
    root.title("Main Menu")
    root.configure(bg='black')

    button1 = tk.Button(root, text="Register Keys", command=lambda: register_keys(), bg='black', fg='#98FB98')
    button1.pack()

    button2 = tk.Button(root, text="Decrypt and Encrypt", command=lambda: create_tk_interface(), bg='black', fg='#98FB98')
    button2.pack()

    button3 = tk.Button(root, text="QR Keys", command=lambda: create_qr_interface(), bg='black', fg='#98FB98')
    button3.pack()

    # Bind Ctrl+W to close the window
    root.bind('<Control-w>', lambda event: root.destroy())

    root.mainloop()