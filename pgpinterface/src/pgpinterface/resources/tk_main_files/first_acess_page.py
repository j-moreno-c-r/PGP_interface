from tkinter import Text, Button, Label
from ttkthemes import ThemedTk
from .tool_functions.absolute_paths import private_key
def first_register():
    global window
    window = ThemedTk(theme="clearlooks")
    window.configure(bg='black')
    window.title("Register Keys")

   

    key_label = Label(window, text="Private Key:", font=("Courier", 14), bg='black', fg='green2')
    key_label.pack()

    key_entry = Text(window, height=10, width=50, font=("Courier", 14), bg='black', fg='green2')
    key_entry.pack()

    def submit_key():
        with open(private_key(), 'w') as key_file:
            key_file.write(key_entry.get("1.0", "end-1c"))  # get text from Text widget
        window.destroy()
    submit_button = Button(window, text="Submit", font=("Courier", 14), bg='black', fg='green2', command=submit_key,  borderwidth=2, relief="groove")
    submit_button.pack()



    window.mainloop()