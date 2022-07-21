from admin1 import *
from user import *
from data import *
van=int(input("""please enter
                 enter 1 for admin
                 enter 2 for user: """))
van11=int(input("""please enter
                 enter 1 for user registration
                 enter 2 for user login: """))
if van == 1:
    admin().admin_login()


elif van == 2:
    if van11 ==1:
        User().user_register()
    elif van11 == 2:
        User().user_login()
    else:
        print("please enter correct option")

else:
    print("please enter correct option")





