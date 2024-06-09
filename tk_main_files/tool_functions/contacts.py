import os
import gnupg
import tkinter as tk
from ttkthemes import ThemedTk

gnupg_home = os.path.join(os.path.expanduser('~'), '.gnupg')
gpg = gnupg.GPG(gnupghome=gnupg_home)

def key_info():
    

    key_info = []
    for key in gpg.list_keys():
        uid = key['uids'][0] if key['uids'] else 'No UID'
        uid = uid.encode('latin1').decode('utf8') 
        name, email = uid.split('<') if '<' in uid else (uid, 'No Email')
        email = email.rstrip('>')
        key_info.append((f'Key_id: {key["keyid"]}, Fingerprint: {key["fingerprint"]}, Name: {name}, Email: {email}'))

    return key_info


def extract_armored_pubkey(contact_text):
    # Extract key id from the contact_text
    key_id = contact_text.split(',')[0].split(':')[1].strip()
    armored_key = gpg.export_keys(key_id)
    with open('keys/public_key.asc', 'w') as key_file:
        key_file.write(armored_key)

def create_the_window_contacts():
    global root
    root = ThemedTk(theme="clearlooks")
    root.configure(bg='black')
    root.title("Main Menu")
    
    ids = key_info()
    for contact_text in ids:
        # Use lambda to pass the contact_text to the function
        submit_button = tk.Button(root, text=contact_text, font=("Courier", 14), bg='black', fg='green2', command=lambda contact_text=contact_text: extract_armored_pubkey(contact_text),  borderwidth=2, relief="groove")
        submit_button.pack()

    root.mainloop()

