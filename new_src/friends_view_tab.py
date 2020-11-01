from tkinter import *
from new_src.databaseOperations import fetch_friends, fetch_user_name, del_from_friends
from tkinter import font


class ViewFriends(Frame):
    def __init__(self, parent, current_user):
        super(ViewFriends, self).__init__(parent)
        self.current_user = current_user
        self.set_up_view_friends()

    def set_up_view_friends(self):
        self.lis = fetch_friends(self.current_user)
        self.friend_names = [fetch_user_name(x[0])[0] for x in self.lis]
        print(self.friend_names)
        Label(self, text="Your friends", font=font.Font(size=25)).pack()
        self.frames = []
        F=Frame(self)
        F.pack()
        f2 = Frame(F)
        f2.pack(side=LEFT)
        f3 = Frame(F)
        f3.pack(side=LEFT)
        self.frames.append(F)
        for x in range(len(self.lis)):
            # F = Frame(self)
            # F.pack()
            # Label(f2,text=self.friend_names[x],font=font.Font(size=20)).pack(fill=X)
            # # Label(F, text=self.friend_names[x], font=font.Font(size=20)).grid(row=x, column=0, padx=20, pady=10)
            # Button(f3,text="Delete Friend",font=font.Font(size=20),command=self.delete_friend_button_clicked(self.lis[x])).pack(fill=X)
            # Button(F, text="remove", font=font.Font(size=15),command=self.delete_friend_button_clicked(self.lis[x])).grid(row=x, column=1, padx=50)
            # self.frames.append(F)
            Label(f2,text=self.friend_names[x],font=font.Font(size=20)).pack(fill=X,padx=10,pady=10)
            Button(f3, text="remove", font=font.Font(size=15),command=self.delete_friend_button_clicked(self.lis[x])).pack(fill=X,padx=10,pady=10)

    def delete_friend_button_clicked(self, email):
        def action_function():
            print(self.current_user)
            del_from_friends(self.current_user, email[0])
            print(email)
        return action_function


root = Tk()
w = ViewFriends(root,"b@gmail")
w.pack()

root.mainloop()
