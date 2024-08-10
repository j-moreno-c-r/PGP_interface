import tkinter as tk
from tkinter import Toplevel, Text, Button, Label
from ttkthemes import ThemedTk
from .tk_qr_menu import create_qr_interface
from .tool_functions.absolute_paths import private_key
def configs_page():
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
            with open(private_key(), 'w') as key_file:
                key_file.write(key_entry.get("1.0", "end-1c"))  # get text from Text widget
            key_window.destroy()
        submit_button = Button(key_window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_key,  borderwidth=2, relief="groove")
        submit_button.pack()


    private_key_button = Button(window, text="Overwrite Private Key", font=("Courier", 14), bg='black', fg='green2', command=open_key_window,  borderwidth=2, relief="groove")
    private_key_button.grid(row=8, column=0, sticky='ew', padx=10, pady=10)
    qr_page_button  = tk.Button(window, text="QR Keys", command=lambda: create_qr_interface(), bg='black', fg='green2', font=('Roboto', 12), borderwidth=2, relief="groove")
    qr_page_button.grid(row=9, column=0, sticky='ew', padx=10, pady=10)

    window.mainloop()