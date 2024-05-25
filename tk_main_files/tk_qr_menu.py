from .tool_functions.qr_keys_output import create_qr_code
import tkinter as tk

with open('keys/private_key.txt', 'r') as file:
    private_key = str(file.read())
with open('keys/public_key.txt', 'r') as file:
    public_key = str(file.read())

def create_qr_interface():
    root = tk.Tk()
    root.title("QR Code Interface")
    root.configure(bg='black')

    button = tk.Button(root, text="QR code Private Key", command=lambda: create_qr_code(private_key,"Private_key", size=3), font=("Courier", 14), bg='black', fg='green2')
    button.pack()
    button2 = tk.Button(root, text="QR code Public Key", command=lambda: create_qr_code(public_key,"Public_key", size=3), font=("Courier", 14), bg='black', fg='green2')
    button2.pack()

    root.bind('<Control-w>', lambda event: root.destroy())

    root.mainloop()