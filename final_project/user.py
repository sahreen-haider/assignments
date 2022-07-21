from data import *
import re
import json


class User:

    # ---user module---

    def __init__(self):
        self.menu = {}
        self.id = 1
        self.ord_lst = {}
        self.user_lst = {}
        self.user_data = {}
        self.neworder = []
        self.order_history={}

    def user_register(self):
        user_name = re.findall("^[A-z]+", input("enter your name:"))

        try:
            if len(user_name) > 0:

                self.user_lst.update({"name": user_name})
                self.user_lst.update({"Phone_number": int(input("please enter your phone number: "))})
                self.user_lst.update({"address": input("please enter your address: ")})
                self.user_lst.update({"password": input("please enter your please enter your password: ")})
                self.user_data.update({input("please enter your email address: "): self.user_lst})
                with open('login_data.txt', 'w') as login_data:
                    login_data.write(json.dumps(self.user_data))

                print(self.user_data)
                User().user_login()
            else:
                print("the name is not inn the correct format")
        except ValueError:
            print("not correct")

    def user_login(self):

        with open('login_data.txt', 'r+') as f:
            dac=f.read()
            data1=json.loads(dac)
            for each, every in data1.items():
                res1=each
                res2=every.get("password")




        if input("please enter your email for the user login: ") == res1:
            if input("please enter your password: ") == res2:
                var1=int(input("""enter 1 for new order
                enter 2 for order history
                enter 3 for updating your profile
                enter 4 to exit"""))
                if var1 == 1:
                    obj1 = data()

                    print(obj1.show_menu())
                    for each in range(int(input("""enter the number of items
                    that you would like to buy: """))):
                        with open(r"menu.txt","r+") as menu_data:
                            oo=menu_data.readlines(int(input("enter index for the order that you want to have: "))-1)
                        self.neworder.append(oo)
                        print("your order is on your way",self.neworder)
                        with open("ord_history.txt", 'a+') as ord_hist:
                            ord_hist.write(self.neworder.__str__())

                elif var1 == 2:
                    with open("ord_history.txt", 'r+') as ord_hist:
                        print(ord_hist.read())

                elif var1 == 3:
                    User.user_register(self)
                elif var1 ==4:
                    print("exited")
                else:
                    print("incorrect choice: ")

            else:
                print("incorrect password")

        else:
            print("the user email address is incorrect")










