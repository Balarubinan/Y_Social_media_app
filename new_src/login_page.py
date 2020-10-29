from tkinter import *
from tkinter import font
from new_src.databaseOperations import fetch_password
from new_src.session_handler import add_session,set_up_current_sessions

class Login_form(Frame):
    def __init__(self,parent):
        self.parent=parent
        super(Login_form, self).__init__(parent)
        self.set_up_login()
        self.bind('<KP_Enter>',self.login_clicked)
        # is not working!!!

    def set_up_login(self):
        Label(self,text="Login to Social Media",font=font.Font(size=25)).pack()
        Label(self,text="Email",font=font.Font(size=20)).pack()
        self.username=Entry(self,font=font.Font(size=20))
        self.username.pack()
        Label(self, text="Passsword", font=font.Font(size=20)).pack()
        self.pswd= Entry(self, font=font.Font(size=20),show='*')
        self.pswd.pack()
        self.login_button=Button(self,text="login",font=font.Font(size=15),command=self.login_clicked)
        self.login_button.pack()

    def login_clicked(self):
        user=self.username.get()
        pass1=self.pswd.get()
        pass2=fetch_password(user)
        print(pass2)
        if pass2==pass1:
            set_up_current_sessions()
            add_session(user)
            print("Login success!!")
            while(True):
                pass
        else:
            print("Wrong passwrod try again")
            self.username.delete(END,0)
            self.pswd.delete(END,0)
            self.username.pack()


# find how to create bind the enter key to the fucntion
# find how to clear the entry Widgets
root=Tk()
w=Login_form(root)
w.pack()
root.mainloop()
#

