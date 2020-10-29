# username=None
# password=None
# email=None
# profile_pic_link=None
# we can't just use it like these cause multiple sessions might be running at the same time
# on the server!!
from new_src.databaseOperations import fetch_user_details
from pickle import loads, dumps


def set_up_current_sessions():
    global current_sessions
    current_sessions = {}


def save_current_user_info(email):
    with open('info.txt', 'wb') as f:
        data = dumps(email)
        f.write(data)


def get_current_user_info():
    with open('info.txt', 'rb') as f:
        data = f.readline()
        data = loads(data)
        # print('b@gmail'==data)
        return data


def add_session(gnemail):
    # gnemail,gnusername, gnpass, gnprof_link=fetch_user_details(gnemail)[0]
    # global current_sessions
    # info_dict={'email':gnemail,'password':gnpass,'username':gnusername,'profile_pic_link':gnprof_link}
    # if gnemail not in current_sessions:
    # current_sessions[gnemail]=info_dict
    #
    # # 'b@gmail':{'email':gnemail,'password':gnpass,'username':gnusername,'profile_pic_link':gnprof_link}
    # print("Session creation successful!!")
    save_current_user_info(gnemail)
    # else:
    #     print("Session aldready saved for user!!")


def get_info_dict(email):
    user = get_current_user_info()
    gnemail, gnpass, gnusername, gnprof_link = fetch_user_details(email)[0]
    info_dict = {'email': gnemail, 'password': gnpass, 'username': gnusername, 'profile_pic_link': gnprof_link}
    return info_dict


def log_out(email):
    global current_sessions
    del current_sessions[email]
    # deletes the entry of the email session!
    # it is considered logged out as the session is not recognised anymore!


def remember_logged_in(email):
    pass
    # finish this function at the very end of the project!

# print(get_current_user_info())

# add_session('b@gmail')
# print(get_info_dict('b@gmail'))
