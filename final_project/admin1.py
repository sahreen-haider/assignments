from data import *

class admin:

    def __init__(self):
        self.admin_lst=[]

    # def admin_register(self):
    #     self.admin_lst.append(input("please enter your email address: "))
    #     self.admin_lst.append(input("please enter your pasword address: "))
    #     print(self.admin_lst)


    def admin_login(self):
        print("""########## welcome admin ##########""")

        if input("please enter your admin id: ") == "admin12":
            if input("please enter your password: ") == "passcode":
                obj=data()
                k1=int(input("""welcome admin
                please enter 1 to add food
                enter 2 to update menu
                enter 3 to view the menu
                enter 4 to remove an item from the menu
                enter 5 to exit """))
                if k1 == 1:
                   obj.menu()
                elif k1 == 2:
                    obj.update_menu()
                elif k1 == 3:
                    obj.show_menu()
                elif k1 == 4:
                    obj.rm_menu()
                    obj.show_menu()
                elif k1 == 5:
                    print("exited")
                else:
                    print('please enter a valid option')
            else:
                print("your password is wrong")

        else:
            print("your admin id is incorrect: ")

