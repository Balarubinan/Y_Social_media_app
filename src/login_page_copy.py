from tkinter import *
from tkinter import font

def set_up_login(root):
    login_frame = Frame(root)
    login_frame.pack()
    ff = font.Font(size=25)

    Label(login_frame, text="Login to App", font=ff,pady=50).pack()
    Label(login_frame, text="Email", font=font.Font(size=15),pady=10).pack()
    email = Entry(login_frame,font=ff)
    email.pack()
    Label(login_frame, text="Password",font=font.Font(size=15),pady=10).pack()
    paswd = Entry(login_frame,show="*",font=ff)
    paswd.pack()

# set_up_login()

