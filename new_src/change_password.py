from tkinter import *
from tkinter import font
from new_src.databaseOperations import fetch_password,change_password

class Change_password_dialog(Frame):
    def __init__(self,parent,email):
        super(Change_password_dialog, self).__init__(parent)
        self.user_email=email
        self.user_pass=fetch_password(email)
        self.setup_pass_change()

    def setup_pass_change(self):
        Label(self,text="Change password",font=font.Font(size=25)).pack()
        self.main_frame=Frame(self)
        self.main_frame.pack()
        Label(self.main_frame,text="Current password: ",font=font.Font(size=15)).grid(pady=10)
        self.cur_pass=Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.cur_pass.grid(row=0,column=1,pady=10)
        Label(self.main_frame,text="New password: ",font=font.Font(size=15)).grid(row=1,column=0,pady=10)
        self.pass1 = Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.pass1.grid(row=1, column=1,pady=10)
        Label(self.main_frame,text="Confirm password: ",font=font.Font(size=15)).grid(row=2,column=0,pady=10)
        self.pass2 = Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.pass2.grid(row=2, column=1,pady=10)
        Button(self,text="Okay",font=font.Font(size=15),command=self.on_submit).pack(pady=10)
        self.notify_label = Label(self, text='', font=font.Font(size=10))
        self.notify_label.pack(side=BOTTOM)

    def on_submit(self):
        if self.cur_pass.get()==self.user_pass:
            if self.pass1.get()==self.pass2.get():
                change_password(self.user_email,self.pass2.get())
            else:
                self.notify_label['fg'] = 'red'
                self.notify_label['text'] = '**Passwords entered do not match!**'
                self.notify_label.pack()
        else:
            self.notify_label['fg']='red'
            self.notify_label['text']='**Wrong password entered**'
            self.notify_label.pack()


# root=Tk()
# Change_password_dialog(root,'b@gmail').pack()
# root.mainloop()