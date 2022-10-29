from tkinter import Tk
from login_register import login_register_form


def create_login_register_window():
    tk = Tk()
    tk.title('Login Form')
    tk.configure(width=600, height=600)
    login_register_form(tk)
    tk.mainloop()


create_login_register_window()
