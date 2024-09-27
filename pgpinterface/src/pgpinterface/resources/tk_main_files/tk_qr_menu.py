from .tool_functions.qr_keys_output import create_qr_code
from .tool_functions.absolute_paths import private_key, public_key
import tkinter as tk
privatekey = private_key()
publickey = public_key()


with open(privatekey, 'r') as file:
    private_key = str(file.read())
with open(publickey, 'r') as file:
    public_key = str(file.read())

def create_qr_interface():
    root = tk.Tk()
    root.title("QR Code Interface")
    root.configure(bg='black')

    button = tk.Button(root, text="QR code Private Key", command=lambda: create_qr_code(privatekey), font=("Courier", 14), bg='black', fg='green2',  borderwidth=2, relief="groove")
    button.pack()
    button2 = tk.Button(root, text="QR code Public Key", command=lambda: create_qr_code(publickey), font=("Courier", 14), bg='black', fg='green2',  borderwidth=2, relief="groove")
    button2.pack()
    

    root.bind('<Control-w>', lambda event: root.destroy())

    root.mainloop()