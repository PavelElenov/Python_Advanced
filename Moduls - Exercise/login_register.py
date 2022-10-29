from tkinter import Button, Label, Entry

from check_data import check_registration, check_login


def clear_window(tk):
    for widget in tk.winfo_children():
        widget.destroy()


def load_first_page(tk):
    clear_window(tk)
    login_register_form(tk)


def register_screen(tk):
    clear_window(tk)
    Label(tk, text='Email').grid(row=0, column=0)
    email = Entry(tk)
    email.grid(row=0, column=1)

    Label(tk, text='Password').grid(row=1, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)

    Label(tk, text='Confirm password').grid(row=2, column=0)
    confirm_password = Entry(tk, show="*")
    confirm_password.grid(row=2, column=1)

    Button(tk, text='Register', command=lambda: check_registration(email, password, confirm_password, tk)). \
        grid(row=4, column=1)
    Button(tk, text='Go on first page', command=lambda: load_first_page(tk)).grid(row=4, column=2)


def login_screen(tk):
    clear_window(tk)
    Label(tk, text='Email').grid(row=0, column=0)
    email = Entry(tk)
    email.grid(row=0, column=1)

    Label(tk, text='Password').grid(row=1, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    Button(tk, text='Login', command=lambda: check_login(email, password, tk)).grid(row=3, column=1)
    Button(tk, text='Go on first page', command=lambda: load_first_page(tk)).grid(row=3, column=2)


def login_register_form(tk):
    Button(tk, text='Login', bg='green', command=lambda: login_screen(tk)).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=lambda: register_screen(tk)).grid(row=0, column=1)
