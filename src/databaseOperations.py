import sqlite3

try:
    con=sqlite3.connect("C:\\Users\\Balarubinan\\PycharmProjects\\SocialMediaApp\\src\\storeDB.db")
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
        cur.execute(f"delete from Friends where frnd1='{frnd1}' and frnd2='{frnd2}")
        cur.execute(f"delete from Friends where frnd1='{frnd2}' and frnd2='{frnd1}")
        con.commit()
    except:
        print("Delete friends error!")

def fetch_friends(given_name):
    lis=[]
    try:
        cur.execute(f"select frnd1 from Friends where frnd2='{given_name}'")
        lis.append(cur.fetchall())
        cur.execute(f"select frnd2 from Friends where frnd1='{given_name}'")
        lis.append(cur.fetchall())
        return lis
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
        for x in frnd_list:
            cur.execute(f"select * from Post where posted_by='{x}' or type='public'")
            lis.extend(cur.fetchall())
    except:
        print("Post fetch error!")

def add_user(email,username,password,profile_pic_link):
    try:
        cur.execute("insert into User values(?,?,?,?)",(email,username,password,profile_pic_link))
        con.commit()
    except:
        print("User add error")

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

def fetch_password(email):
    try:
        cur.execute(f"select password from User where email='{email}'")
        return cur.fetchall()[0] # 0 contains the password!
    except:
        print("User fetch pass error!")

# type in the stuff for the request DB okay??
# don't forget to explain about auto commit

# add_user('b@gmail','Bala','jjj','acadc')













