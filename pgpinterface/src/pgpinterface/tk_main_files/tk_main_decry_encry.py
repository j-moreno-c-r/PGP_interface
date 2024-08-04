import tkinter as tk
from .tk_encrypt_decrypt import  create_decrypt_interface
from .tk_contacts import create_the_window_contacts
def main_window():
    window = tk.Tk()
    window.title("Encryptio Decryption Menu")
    window.configure(bg='black')

    encrypt_button = tk.Button(window, text="Open Encryption Window", command=create_the_window_contacts, font=("Courier", 14), bg='black', fg='green2')
    decrypt_button = tk.Button(window, text="Open Decryption Window", command=create_decrypt_interface, font=("Courier", 14), bg='black', fg='green2')

    encrypt_button.pack(padx=10, pady=10)
    decrypt_button.pack(padx=10, pady=10)

    window.mainloop()

