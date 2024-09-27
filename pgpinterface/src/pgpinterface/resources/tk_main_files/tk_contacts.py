import tkinter as tk
import gnupg
from tkinter import Toplevel, Text, Button, Label
from ttkthemes import ThemedTk
from .tool_functions.contacts import create_the_window_contacts
from .tool_functions.absolute_paths import public_key
publickey = public_key()
def contacts_page():
    global window
    window = ThemedTk(theme="clearlooks")
    window.configure(bg='black')
    window.title("Contacts")

    def open_public_key_window():
        public_key_window = Toplevel(window)
        public_key_window.title("Register Recipient's Public Key")
        public_key_window.configure(bg='black')

        public_key_label = Label(public_key_window, text="Recipient's Public Key:", font=("Courier", 14), bg='black', fg='green2')
        public_key_label.pack()

        public_key_entry = Text(public_key_window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2', highlightbackground='red', highlightcolor='red', highlightthickness=2)
        public_key_entry.pack()


        def submit_public_key():
            gpg = gnupg.GPG()

            pub_key = public_key_entry.get("1.0", "end-1c")  # get text from Text widget

            # Check if the key is already in the keyring
            key_already_in_keyring = any(key['fingerprint'] == pub_key for key in gpg.list_keys())

            if not key_already_in_keyring:
                # Import the key
                import_result = gpg.import_keys(pub_key)

                if import_result.count != 1:
                    raise ValueError("Failed to import the public key")

            # Write the key to a file
            with open(publickey, 'w') as key_file:
                key_file.write(publickey)

            public_key_window.destroy()
            
        submit_button = Button(public_key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_public_key,  borderwidth=2, relief="groove")
        submit_button.pack()

    
    public_key_button = Button(window, text="Register Recipient's Public Key", font=("Courier", 14), bg='black', fg='green2', command=open_public_key_window,  borderwidth=2, relief="groove")
    public_key_button.grid(row=9, column=0, sticky='ew', padx=10, pady=10)

    select_contacts_button = Button(window, text="Select a Contact", font=("Courier", 14), bg='black', fg='green2', command=create_the_window_contacts,  borderwidth=2, relief="groove")
    select_contacts_button.grid(row=9, column=5, sticky='ew', padx=10, pady=10)
    window.mainloop()