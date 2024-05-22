import tkinter as tk
import base64
from encrypt_decrypt import encrypt, decrypt
from tkinter import Toplevel, Text, Button, Label
def create_tk_interface():
    window = tk.Tk()
    window.title("Encryption and Decryption")
    window.configure(bg='black')

    message_label = tk.Label(window, text="Enter message:", font=("Courier", 14), bg='black', fg='green2')
    message_entry = tk.Entry(window, font=("Courier", 14), bg='black', fg='green2', insertbackground='green2')
    encrypted_label = tk.Label(window, text="Encrypted message:", font=("Courier", 14), bg='black', fg='green2')
    encrypted_message_text = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', wrap='word')
    decrypted_label = tk.Label(window, text="Decrypted message:", font=("Courier", 14), bg='black', fg='green2')
    decrypted_message_text = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', wrap='word')

    encrypted_scrollbar = tk.Scrollbar(window, command=encrypted_message_text.yview)
    decrypted_scrollbar = tk.Scrollbar(window, command=decrypted_message_text.yview)
    encrypted_message_text['yscrollcommand'] = encrypted_scrollbar.set
    decrypted_message_text['yscrollcommand'] = decrypted_scrollbar.set


    def encrypt_message():
        message = message_entry.get("1.0", tk.END)
        encrypted_message = encrypt(message)
        encrypted_message = base64.b64encode(encrypted_message).decode()
        encrypted_message = f"-----BEGIN PGP MESSAGE-----\n\n{encrypted_message}\n-----END PGP MESSAGE-----"
        encrypted_message_text.insert(tk.END, encrypted_message)

    def decrypt_message():
        encrypted_message = encrypted_message_text.get("1.0", tk.END)
        encrypted_message = encrypted_message.replace("-----BEGIN PGP MESSAGE-----\n\n", "").replace("\n-----END PGP MESSAGE-----", "")
        encrypted_message = base64.b64decode(encrypted_message)
        decrypted_message = decrypt(encrypted_message)
        decrypted_message_text.insert(tk.END, decrypted_message)

    def close_window(event):
        window.destroy()

    window.bind('<Control-w>', close_window)
    
    def open_key_window():
        key_window = Toplevel(window)
        key_window.title("Register Private Key")
        key_window.configure(bg='black')

        key_label = Label(key_window, text="Private Key:", font=("Courier", 14), bg='black', fg='green2')
        key_label.pack()

        key_entry = Text(key_window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2')
        key_entry.pack()

        def submit_key():
            with open('private_key.txt', 'w') as key_file:
                key_file.write(key_entry.get("1.0", "end-1c"))  # get text from Text widget
            key_window.destroy()
        submit_button = Button(key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_key)
        submit_button.pack()

    

    def open_public_key_window():
        public_key_window = Toplevel(window)
        public_key_window.title("Register Recipient's Public Key")
        public_key_window.configure(bg='black')

        public_key_label = Label(public_key_window, text="Recipient's Public Key:", font=("Courier", 14), bg='black', fg='green2')
        public_key_label.pack()

        public_key_entry = Text(public_key_window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2', highlightbackground='red', highlightcolor='red', highlightthickness=2)
        public_key_entry.pack()

        def submit_public_key():
            with open('public_key.txt', 'w') as key_file:
                key_file.write(public_key_entry.get("1.0", "end-1c"))  # get text from Text widget
            public_key_window.destroy()

        submit_button = Button(public_key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_public_key)
        submit_button.pack()



    public_key_button = Button(window, text="Register Recipient's Public Key", font=("Courier", 14), bg='black', fg='green2', command=open_public_key_window)
    public_key_button.grid(row=9, column=0, sticky='ew', padx=10, pady=10)
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure((4, 7), weight=1)
    
    encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message, font=("Courier", 14), bg='black', fg='green2')
    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message, font=("Courier", 14), bg='black', fg='green2')
    message_entry = tk.Text(window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2', highlightbackground='red', highlightcolor='red', highlightthickness=2)
    message_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    message_entry.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
    encrypt_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
    encrypted_label.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    encrypted_message_text.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
    encrypted_scrollbar.grid(row=4, column=1, sticky='ns', padx=10, pady=10)
    decrypt_button.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
    decrypted_label.grid(row=6, column=0, sticky='w', padx=10, pady=10)
    decrypted_message_text.grid(row=7, column=0, sticky='nsew', padx=10, pady=10)
    decrypted_scrollbar.grid(row=7, column=1, sticky='ns', padx=10, pady=10)
    private_key_button = Button(window, text="Register Private Key", font=("Courier", 14), bg='black', fg='green2', command=open_key_window)
    private_key_button.grid(row=8, column=0, sticky='ew', padx=10, pady=10)



    window.mainloop()