import json
from tkinter import Label, END


def check_registration(email, password, confirm_password, tk):
    current_email = email.get()
    current_password = password.get()
    current_confirm_password = confirm_password.get()
    if current_password != current_confirm_password:
        Label(tk, text='Incorrect password!!!Try again', fg='red').grid(row=3, column=1)
        confirm_password.delete(0, END)
        password.delete(0, END)
        return
    else:
        data = {'email': current_email, 'password': current_password}
        user = json.dumps(data)

        with open('./users_data.txt') as file:
            if user in file.read():
                Label(tk, text='You are already registered!!!Please login!', fg='red').grid(row=3, column=1)
            else:
                with open('./users_data.txt', 'a') as file_write:
                    file_write.write(user + '\n')
                    file_write.close()
                    Label(tk, text='You are registered!!!', fg='red').grid(row=3, column=1)
            file.close()


def check_login(email, password, tk):
    current_email = email.get()
    current_password = password.get()

    with open('./users_data.txt') as file:
        for line in file:
            line = json.loads(line)
            if line['email'] == current_email:
                if line['password'] == current_password:
                    Label(tk, text='You are logged in!!!', fg='red').grid(row=2, column=1)
                    break
                else:
                    Label(tk, text='Incorrect password!!!', fg='red').grid(row=2, column=1)
                    password.delete(0, END)
                    break
        else:
            Label(tk, text='Incorrect email!!! You can register!', fg='red').grid(row=2, column=1)
