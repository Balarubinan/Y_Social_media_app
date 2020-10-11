from tkinter import *
from tkinter import font
from new_src.databaseOperations import add_user


# username,pass1,pass2,email,parent_copy=None,None,None,None,None

class Sign_up_page(Frame):
    def __init__(self,parent):
        super(Sign_up_page, self).__init__(parent)
        self.set_up_sign_up_form(self)
        self.parent=parent

    def set_up_sign_up_form(self,parent):
        # global username,pass1,pass2,email
        parent_copy = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        # user,passs,email,prof pic (optional)
        self.small = font.Font(size=15)
        self.big = font.Font(size=25)
        Label(self.main_frame, text="Sign Up", font=font.Font(size=25)).pack()
        Label(self.main_frame, text="Email", font=self.small).pack()
        self.email = Entry(self.main_frame, font=self.big)
        self.email.pack()
        Label(self.main_frame, text="Username", font=self.small).pack()
        self.username = Entry(self.main_frame, font=self.big)
        self.username.pack()
        Label(self.main_frame, text="Password", font=self.small).pack()
        self.pass1 = Entry(self.main_frame, show='*', font=self.big)
        self.pass1.pack()
        Label(self.main_frame, text="Re-type Password", font=self.small).pack()
        self.pass2 = Entry(self.main_frame, show='*', font=self.big)
        self.pass2.pack()
        # profile pic to be added
        self.sign_up_button = Button(self.main_frame, text="Sign up", font=self.small, command=self.sign_up_clicked)
        self.sign_up_button.pack()

    def sign_up_clicked(self):
        # global username,pass1,pass2,email
        print(self.pass1.get(), self.pass2.get())
        if self.pass1.get() != self.pass2.get():
            print("Passswords don't match")
            self.set_up_sign_up_form(self.parent)
            return
        res = add_user(email=self.email.get(), username=self.username.get(), password=self.pass1.get(), profile_pic_link="NO_IMAGE")
        if res:
            print("User sign_up_success!")
        else:
            print("User not added email aldready exists!")
            self.set_up_sign_up_form(self.parent)


# root=Tk()
# w=Sign_up_page(root)
# w.pack()
# root.mainloop()
