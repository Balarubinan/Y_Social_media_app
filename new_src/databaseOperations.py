import sqlite3
from pickle import dumps,loads

try:
    con=sqlite3.connect("C:\\Users\\Balarubinan\\PycharmProjects\\SocialMediaApp\\new_src\\storeDB.db")
    cur=con.cursor()
    # con.row_factory=sqlite3.Row
except:
    print("DB connect error!")

def add_comment(post_id,comment,username):
    try:
        cur.execute(f"insert into Comment values('{post_id}','{comment}','{username}')")
        con.commit()
    except:
        print("Comment add error!")

def delete_comment(post_id,username):
    try:
        cur.execute(f"delete from Comment where post_id='{post_id}' and username='{username}'")
        con.commit()
    except:
        print("Delete error!")

def add_to_friends(frnd1,frnd2):
    try:
        cur.execute(f"insert into Friends values('{frnd1}','{frnd2}')")
        con.commit() 
    except:
        print("add friends error!")

def del_from_friends(frnd1,frnd2):
    try:
        cur.execute(f"delete from Friends where frnd1='{frnd1}' and frnd2='{frnd2}'")
        # cur.execute(f"delete from Friends where frnd1='{frnd2}' and frnd2='{frnd1}")
        con.commit()
    except:
        print("Delete friends error!")

def fetch_friends(given_name):
    lis=[]
    try:
        # cur.execute(f"select frnd1 from Friends where frnd2='{given_name}'")
        # lis.append(cur.fetchall())
        cur.execute(f"select frnd2 from Friends where frnd1='{given_name}'")
        return cur.fetchall()
    except:
        print("search friends error!")

def add_image(id,posted_by,type,path):
    try:
        cur.execute(f"insert into Images values(?,?,?,?)",(id,posted_by,type,path))
        con.commit()
    except:
        print("add_image error!")

def del_image(id):
    try:
        cur.execute(f"delete from Images where id='{id}'")
        con.commit()
    except:
        print("Error del_image")

# explain after here

def add_post(post_id,posted_by,type,caption,likes,images_id):
    try:
        cur.execute("insert into Post values(?,?,?,?,?,?)",(post_id,posted_by,type,caption,likes,images_id))
        con.commit()
    except:
        print("Add post error!")

def delete_post(post_id):
    try:
        cur.execute(f"delete from Post where post_id='{post_id}'")
        con.commit()
    except:
        print("Post delete error")

def fetch_user_posts(frnd_list):
    try:
        lis=[]
        # for every friend the public posts get fetched again and again
        # as post_id's are unique we can track duplicate post this way
        # fetch_list maintains a list of all the post_id's fetched so far
        fetch_list=[]
        print("friend list:",frnd_list)
        for x in frnd_list:
            cur.execute(f"select * from Post where posted_by='{x}' or type='public'")
            val=cur.fetchall()
            if val[0] not in fetch_list:
                # adding result iff post_id is new
                lis.extend(val)
                fetch_list.append(val[0])
        print("returned list is ",lis)
        return lis
    except:
        print("Post fetch error!")

def add_user(email,username,password,profile_pic_link):
    try:
        cur.execute("insert into User values(?,?,?,?)",(email,username,password,profile_pic_link))
        con.commit()
        return True
    except:
        print("User add error")
        return False

def del_user(email):
    try:
        cur.execute(f"delete from User where email='{email}'")
    except:
        print("User del error")

def fetch_user_details(email):
    try:
        cur.execute(f"select * from User where email='{email}'")
        return cur.fetchall()
    except:
        print("User fetch error!")

def fetch_user_name(email):
    # try:
    cur.execute(f"select username from User where email='{email}'")
    return cur.fetchall()
    # except:
    #     print("User name fetch error!")

def fetch_password(email):
    try:
        cur.execute(f"select password from User where email='{email}'")
        # print(cur.fetchall()[0])
        return cur.fetchall()[0][0] # 0 contains the password!#

    except:
        print("User fetch pass error!")

def fetch_starts_with(string):
    try:
        con2 = sqlite3.connect("C:\\Users\\Balarubinan\\PycharmProjects\\SocialMediaApp\\new_src\\storeDB.db")
        cur2 = con2.cursor()
        cur2.execute(f"select username,profile_pic_link,email from User where email like '{string}%' or username like '{string}%'")
        return cur2.fetchall()
    except:
        print("Fetch Error! like")
        return []

def add_to_request(email1,email2):
    try:
        cur.execute(f"insert into Requests values('{email1}','{email2}')")
        con.commit()
    except:
        print("Add to requests error!")

def fetch_from_requests(email):
    try:
        cur.execute(f"select frnd2 from Requests where frnd1='{email}'")
        return cur.fetchall()
    except:
        print("Error in fetch request!")

def del_from_request(email1,email2):
    try:
        cur.execute(f"delete from Requests where frnd1='{email1}' and frnd2='{email2}'")
        con.commit()
    except:
        print("Error in del_request request!")

def increase_like(post_id):
    try:
        cur.execute(f"update Post set likes=likes+1 where post_id='{post_id}'")
        con.commit()
    except:
        print("Update error!")

def fetch_post_by_id(post_id):
    try:
        cur.execute(f"select * from Post where post_id='{post_id}'")
        return cur.fetchall()[0]
    except:
        print("Update error!")


def fetch_comments(post_id):
    try:
        cur.execute(f"select * from comment where post_id='{post_id}'")
        return cur.fetchall()
    except:
        print("fetch comment error error!")

# post_id table functions

def update_last_postid():
    try:
        cur.execute(f"update Last_post set last_id=last_id+1")
        con.commit()
    except:
        print("Last_post_id update error")

def get_new_post_id():
    try:
        cur.execute(f"select * from Last_post")
        return int(cur.fetchall()[0][0])
    except:
        print("Last_post_id update error")

def update_user_profile_pic(email,path):
    try:
        # path=dumps(path)
        cur.execute(f"select * from Userpic where posted_by='{email}'")
        if len(cur.fetchall())>0:
            cur.execute(f"update Userpic set path='{path}' where posted_by='{email}'")
            con.commit()
        else:
            cur.execute(f"insert into Userpic values('{email}','{path}')")
            con.commit()
    except:
        print("User pic update error!")

def change_password(email,password):
    try:
        cur.execute(f"update User set password='{password}' where email='{email}'")
        con.commit()
    except:
        print("Change password error!!!")

def change_username(email,new_name):
    try:
        cur.execute(f"update User set username='{new_name}' where email='{email}'")
        con.commit()
    except:
        print("Change username error!!!")

def get_user_prof_pic(email):
    try:
        cur.execute(f"select path from Userpic where posted_by='{email}'")
        return(cur.fetchall()[0][0])
    except:
        print("prof pic get error!")






# change_password('rick@gmail.com',"ricky!")

# update_user_profile_pic('rick@gmail.com',"this//seems//like//a path")
# type in the stuff for the request DB okay??
# don't forget to explain about auto commit

# add_user('b@gmail','Bala','jjj','acadc')
# print(fetch_starts_with('as'))
# print(fetch_friends("b@gmail"))
# del_from_friends('b@gamil',)













