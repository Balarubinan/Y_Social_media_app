from tkinter import *
from new_src.databaseOperations import fetch_friends,fetch_user_name,del_from_friends
from tkinter import font

class ViewFriends(Frame):
    def __init__(self,parent,current_user):
        super(ViewFriends, self).__init__(parent)
        self.current_user=current_user
        self.set_up_view_friends()

    def set_up_view_friends(self):
        self.lis=fetch_friends(self.current_user)
        self.friend_names=[fetch_user_name(x[0])[0] for x in self.lis]
        print(self.friend_names)
        self.frames=[]
        for x in range(len(self.lis)):
            F=Frame(self)
            F.pack()
            Label(F,text=self.friend_names[x],font=font.Font(size=20)).pack(side=LEFT)
            Button(F,text="Delete Friend",font=font.Font(size=20),command=self.delete_friend_button_clicked(self.lis[x])).pack(side=LEFT)
            self.frames.append(F)

    def delete_friend_button_clicked(self,email):
        def action_function():
            print(self.current_user)
            del_from_friends(self.current_user,email[0])
            print(email)
        return action_function

root=Tk()
w=ViewFriends(root,"b@gmail")
w.pack()

root.mainloop()



