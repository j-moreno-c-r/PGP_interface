import os
import gnupg
import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame, CENTER
from ttkthemes import ThemedTk
from  ..tk_encrypt_decrypt import create_encrypt_interface 

gnupg_home = os.path.join(os.path.expanduser('~'), '.gnupg')
gpg = gnupg.GPG(gnupghome=gnupg_home)

def key_info():
    

    key_info = []
    for key in gpg.list_keys():
        uid = key['uids'][0] if key['uids'] else 'No UID'
        uid = uid.encode('latin1').decode('utf8') 
        name, email = uid.split('<') if '<' in uid else (uid, 'No Email')
        email = email.rstrip('>')
        key_info.append(f'''
        Key_id: {key["keyid"]},
        Fingerprint: {key["fingerprint"]},
        Name: {name},
        Email: {email}
        ''')

    return key_info


def extract_armored_pubkey(contact_text):
    # Extract key id from the contact_text
    key_id = contact_text.split(',')[0].split(':')[1].strip()
    armored_key = gpg.export_keys(key_id)
    with open('keys/public_key.asc', 'w') as key_file:
        key_file.write(armored_key)
        import_result = gpg.import_keys(armored_key)
    with open('keys/fingerprint_pubkey.asc', 'w') as key_file:
        key_fingerprint = import_result.fingerprints[0]
        key_file.write(key_fingerprint)



from tkinter import Tk, Frame, Button, Scrollbar, Canvas
from tkinter.constants import N, S, E, W

def create_the_window_contacts():
    global root
    root = Tk()
    root.configure(bg='black')
    root.geometry("1200x500")
    root.title("Main Menu")

    # Create a main frame
    main_frame = Frame(root, bg='black')
    main_frame.pack(fill='both', expand=True)

    # Create a canvas inside the main frame
    my_canvas = Canvas(main_frame, bg='black')
    my_canvas.pack(side='left', fill='both', expand=True)

    # Add a scrollbar to the canvas
    my_scrollbar = Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.pack(side='right', fill='y')

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    second_frame = Frame(my_canvas, bg='black')

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

    ids = key_info()
    for i, contact_text in enumerate(ids):
        # Use lambda to pass the contact_text to the function
        submit_button = Button(second_frame, text=contact_text, font=("Courier", 14), bg='black', fg='green2', command=lambda contact_text=contact_text: extract_armored_pubkey(contact_text),  borderwidth=2, relief="groove")
        submit_button.grid(row=i, column=0, sticky='nsew')

    button_follow = Button(second_frame, text="follow to the encrypt page", font=("Courier", 14), bg='black', fg='green2', command=create_encrypt_interface,  borderwidth=2, relief="groove")
    button_follow.grid(row=len(ids), column=0, sticky='nsew')

    # Configure the grid to expand the buttons
    second_frame.grid_columnconfigure(0, weight=1)

    root.mainloop()