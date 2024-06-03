import tkinter as tk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from .tk_contacts import contacts_page
from .tk_configs import configs_page 
from .first_acess_page import first_register
from .tk_main_decry_encry import main_window

def create_main_menu():
    global root
    root = ThemedTk(theme="clearlooks")
    root.configure(bg='black')
    root.title("Main Menu")
    with open('keys/private_key.asc', 'r') as file:
        private_key = str(file.read())

        
    if private_key == "":
        first_register()
        


    # Add background image
    image = Image.open("images/main_bg.jpeg")
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.geometry("%dx%d" % (image.width, image.height))


    button_read_write = tk.Button(root, text="Read/write", command=lambda: main_window(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button_read_write.place(x=20, y=60) 

    button_contacts = tk.Button(root, text="Contacts", command=lambda: contacts_page(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button_contacts.place(x=20, y=20)  

    button_configs = tk.Button(root, text='Configs',command=lambda: configs_page(), bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=2, relief="groove")
    button_configs.place(x=20, y=100)

    tutorial_text = "Wake Up, Neo...\n The Matrix has you...\n Follow the white rabbit...\n Knock, knock, Neo." 
    tutorial_label = tk.Label(root, text=tutorial_text, bg='black', fg='#98FB98', font=('Roboto', 12), borderwidth=5, relief="groove")
    tutorial_label.place(x=18, y=140)  

    # Bind Ctrl+W to close the window
    root.bind('<Control-w>', lambda event: root.destroy())

    root.mainloop()