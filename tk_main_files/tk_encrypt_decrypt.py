import tkinter as tk
from .tool_functions.encrypt_decrypt import encrypt_message, decrypt_message
from .tool_functions.qr_keys_output import create_qr_code

def create_encrypt_interface():
    window = tk.Tk()
    window.title("Encryption")
    window.configure(bg='black')

    message_label = tk.Label(window, text="Enter message:", font=("Courier", 14), bg='black', fg='green2')
    message_entry = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', insertbackground='green2')
    encrypted_label = tk.Label(window, text="Encrypted message:", font=("Courier", 14), bg='black', fg='green2')
    encrypted_message_text = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', wrap='word')

    encrypted_scrollbar = tk.Scrollbar(window, command=encrypted_message_text.yview)
    encrypted_message_text['yscrollcommand'] = encrypted_scrollbar.set
    def gtc(dtxt):
        window.clipboard_clear()
        window.clipboard_append(dtxt)

    def encrypt_message_tk():
        message = message_entry.get("1.0", tk.END)
        encrypted_message = encrypt_message(message, 'keys/fingerprint_pubkey.asc')
        encrypted_message = encrypted_message
        encrypted_message_text.insert(tk.END, encrypted_message)

    def close_window(event):
        window.destroy()

    window.bind('<Control-w>', close_window)

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure((4, 7), weight=1)

    encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message_tk, font=("Courier", 14), bg='black', fg='green2',  borderwidth=2, relief="groove")
    message_entry = tk.Text(window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2', highlightbackground='red', highlightcolor='red', highlightthickness=2)
    message_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    message_entry.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
    encrypt_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
    encrypted_label.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    encrypted_message_text.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
    encrypted_scrollbar.grid(row=4, column=1, sticky='ns', padx=10, pady=10)
    copy_button = tk.Button(window, text="Copy", command=lambda: gtc(encrypted_message_text.get("1.0", tk.END)), font=("Courier", 14), bg='black', fg='green2', borderwidth=2, relief="groove")
    encrypted_scrollbar.grid(row=4, column=1, sticky='ns', padx=10, pady=10)
    copy_button.grid(row=5, column=0, sticky='ew', padx=10, pady=10)


    window.mainloop()

def create_decrypt_interface():
    global encrypted_for_qr
    window = tk.Tk()
    window.title("Decryption")
    window.configure(bg='black')
    

    encrypted_label = tk.Label(window, text="Enter encrypted message:", font=("Courier", 14), bg='black', fg='green2')
    encrypted_message_entry = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', insertbackground='green2')
    decrypted_label = tk.Label(window, text="Decrypted message:", font=("Courier", 14), bg='black', fg='green2')
    decrypted_message_text = tk.Text(window, font=("Courier", 14), bg='black', fg='green2', wrap='word')
    def get_text_from_entry():
        global text_qr
        text = encrypted_message_entry.get("1.0", tk.END)
        return text
    text_qr = get_text_from_entry()
    button = tk.Button(window, text="Qr encripted message", command=lambda: create_qr_code(text_qr,v=15), font=("Courier", 14), bg='black', fg='green2')


    decrypted_scrollbar = tk.Scrollbar(window, command=decrypted_message_text.yview)
    decrypted_message_text['yscrollcommand'] = decrypted_scrollbar.set

    def decrypt_message_tk():
        encrypted_message = encrypted_message_entry.get("1.0", tk.END)
        encrypted_message = encrypted_message
        decrypted_message = decrypt_message(encrypted_message, 'keys/private_key.asc')
        decrypted_message_text.insert(tk.END, decrypted_message)
    def close_window(event):
        window.destroy()

    window.bind('<Control-w>', close_window)

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure((4, 7), weight=1)

    
    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message_tk, font=("Courier", 14), bg='black', fg='green2',  borderwidth=2, relief="groove")
    encrypted_message_entry = tk.Text(window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2', highlightbackground='red', highlightcolor='red', highlightthickness=2)
    encrypted_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    button.grid(row=0, column=1, sticky='w', padx=10, pady=10)
    encrypted_message_entry.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
    decrypt_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
    decrypted_label.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    decrypted_message_text.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
    decrypted_scrollbar.grid(row=4, column=1, sticky='ns', padx=10, pady=10)
    

    window.mainloop()