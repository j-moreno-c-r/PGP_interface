import tkinter as tk
from tk_encrypt_decrypt import create_encrypt_interface, create_decrypt_interface

def main_window():
    window = tk.Tk()
    window.title("Main Window")
    window.configure(bg='black')

    def open_encrypt_window():
        create_encrypt_interface()

    def open_decrypt_window():
        create_decrypt_interface()

    encrypt_button = tk.Button(window, text="Open Encryption Window", command=open_encrypt_window, font=("Courier", 14), bg='black', fg='green2')
    decrypt_button = tk.Button(window, text="Open Decryption Window", command=open_decrypt_window, font=("Courier", 14), bg='black', fg='green2')

    encrypt_button.pack(padx=10, pady=10)
    decrypt_button.pack(padx=10, pady=10)

    window.mainloop()

