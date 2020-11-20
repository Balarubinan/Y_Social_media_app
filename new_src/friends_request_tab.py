from tkinter import *
from tkinter import font
from new_src.databaseOperations import fetch_from_requests,add_to_friends,del_from_request

class RequestTab(Frame):
    def __init__(self,parent,currentuser):
        super(RequestTab, self).__init__(parent)
        self.current_user=currentuser
        self.frames=[]
        self.setup_request_tab()

    def setup_request_tab(self):
        self.res=fetch_from_requests(self.current_user)
        for x in self.res:
            f=Frame(self)
            f.pack(pady=10)
            Label(f,text=x[0],font=font.Font(size=20)).pack(side=LEFT,padx=10)
            Button(f,text="Accept",font=font.Font(size=20),command=self.accept_clicked(x[0])).pack(side=LEFT,padx=10)
            Button(f,text="Decline",font=font.Font(size=20),command=self.decline_clicked(x[0])).pack(side=LEFT,padx=10)
            self.frames.append(f)

    def accept_clicked(self,email):
        def action_function1():
            add_to_friends(self.current_user,email)
            del_from_request(self.current_user,email)
            self.pack_forget()
        return action_function1

    def decline_clicked(self,email):
        def action_function2():
            del_from_request(self.current_user,email)
            self.pack_forget()
        return action_function2

# root=Tk()
# RequestTab(root,'b@gmail').pack()
# root.mainloop()

