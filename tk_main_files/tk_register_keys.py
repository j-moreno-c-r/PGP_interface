import tkinter as tk
from tkinter import Toplevel, Text, Button, Label
from ttkthemes import ThemedTk
def register_keys():
    global window
    window = ThemedTk(theme="clearlooks")
    window.configure(bg='black')
    window.title("Register Keys")

    def open_key_window():
        key_window = Toplevel(window)
        key_window.title("Register Private Key")
        key_window.configure(bg='black')

        key_label = Label(key_window, text="Private Key:", font=("Courier", 14), bg='black', fg='green2')
        key_label.pack()

        key_entry = Text(key_window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2')
        key_entry.pack()

        def submit_key():
            with open('keys/private_key.txt', 'w') as key_file:
                key_file.write(key_entry.get("1.0", "end-1c"))  # get text from Text widget
            key_window.destroy()
        submit_button = Button(key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_key,  borderwidth=2, relief="groove")
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
            with open('keys/public_key.txt', 'w') as key_file:
                key_file.write(public_key_entry.get("1.0", "end-1c"))  # get text from Text widget
            public_key_window.destroy()

        submit_button = Button(public_key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_public_key,  borderwidth=2, relief="groove")
        submit_button.pack()

    private_key_button = Button(window, text="Register Private Key", font=("Courier", 14), bg='black', fg='green2', command=open_key_window,  borderwidth=2, relief="groove")
    private_key_button.grid(row=8, column=0, sticky='ew', padx=10, pady=10)
    public_key_button = Button(window, text="Register Recipient's Public Key", font=("Courier", 14), bg='black', fg='green2', command=open_public_key_window,  borderwidth=2, relief="groove")
    public_key_button.grid(row=9, column=0, sticky='ew', padx=10, pady=10)

    window.mainloop()