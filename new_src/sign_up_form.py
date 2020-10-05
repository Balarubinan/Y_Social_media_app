from tkinter import *
from tkinter import font
from new_src.databaseOperations import add_user


username,pass1,pass2,email,parent_copy=None,None,None,None,None

def set_up_sign_up_form(parent):
    global username,pass1,pass2,email
    parent_copy=parent
    main_frame=Frame(parent)
    main_frame.pack()
    # user,passs,email,prof pic (optional)
    small=font.Font(size=15)
    big=font.Font(size=25)
    Label(main_frame,text="Sign Up",font=font.Font(size=25)).pack()
    Label(main_frame,text="Email",font=small).pack()
    email=Entry(main_frame,font=big)
    email.pack()
    Label(main_frame, text="Username", font=small).pack()
    username=Entry(main_frame,font=big)
    username.pack()
    Label(main_frame, text="Password", font=small).pack()
    pass1=Entry(main_frame,show='*',font=big)
    pass1.pack()
    Label(main_frame, text="Re-type Password", font=small).pack()
    pass2 = Entry(main_frame,show='*',font=big)
    pass2.pack()
    # profile pic to be added
    sign_up_button=Button(main_frame,text="Sign up",font=small,command=sign_up_clicked)
    sign_up_button.pack()


def sign_up_clicked():
    global username,pass1,pass2,email
    print(pass1.get(),pass2.get())
    if pass1.get()!=pass2.get():
        print("Passswords don't match")
        set_up_sign_up_form(parent_copy)
        return
    res=add_user(email=email.get(),username=username.get(),password=pass1.get(),profile_pic_link="NO_IMAGE")
    if res:
        print("User sign_up_success!")
    else:
        print("User not added email aldready exists!")
        set_up_sign_up_form(parent_copy)


root=Tk()
set_up_sign_up_form(root)
root.mainloop()
