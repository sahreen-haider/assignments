import re
import json

class data:
    def __init__(self):
        self.ord_lst={}
        self.menu1 = {}
        self.id=1


    def menu(self):
        try:
            # items_count = int(input("the no of items that need to be added: "))
            # y = 1
            # while y <= items_count:
            name = re.findall("^[A-z]+", input("enter the name for the food: "))
            if len(name) > 0:

                self.ord_lst.update({"name": name})
                self.ord_lst.update({"Stock": int(input("please enter the stock for the food item: "))})
                self.ord_lst.update({"Price": float(input("please enter the price: "))})
                f=int(input("""please enter the quantity for the food
                enter 1 for 100 ml
                enter 2 for 150 ml
                enter 3 for 250 ml"""))

                if f==1:
                    self.ord_lst.update({"Quantity": "100ml"})
                elif f==2:
                    self.ord_lst.update({"Quantity": "150ml"})
                elif f==3:
                    self.ord_lst.update({"Quantity": "250ml"})
                self.ord_lst.update({"Discount": float(input("""please enter the discount 
                for the specified food: """))})
                print(self.ord_lst)
                self.menu1.update({self.id: self.ord_lst})
                self.id += 1
                print(self.menu1)

                with open("menu.txt", "a+") as menu_data:
                    menu_data.write(json.dumps(self.menu1))
                    menu_data.write("\n")
            else:
                print("the name is not in the correct format")

                # y += 1
        except ValueError:
            print("not correct")

    def show_menu(self):
        with open("menu.txt","r+") as menu_data:
            res=menu_data.readlines()
            if len(res)>0:
                for each in res:
                    print(each)
            else:
                print("""opsie!
                         we are out of the stock
                         please come again later
                         or ask the admin to add some stock to the menu""")
        # # rev=json.loads(rec)
        # print(rev)





    def update_menu(self):
        data().show_menu()
        with open(r"menu.txt", "r+") as menu_data:
            local1 = menu_data.readlines()
            data().show_menu()
            menu_data.seek(0)
            menu_data.truncate()
            menu_data.writelines(local1[:int(input("enter index no")) - 1])

        name = re.findall("^[A-z]+", input(f"enter the name for the food: "))
        self.ord_lst.update({"name": name})
        self.ord_lst.update({"Stock": int(input("please enter the stock for the food item: "))})
        self.ord_lst.update({"Price": float(input("please enter the price: "))})
        f = int(input("""please enter the quantity for the food
                            enter 1 for 100 ml
                            enter 2 for 150 ml
                            enter 3 for 250 ml"""))

        if f == 1:
            self.ord_lst.update({"Quantity": "100ml"})
        elif f == 2:
            self.ord_lst.update({"Quantity": "150ml"})
        elif f == 3:
            self.ord_lst.update({"Quantity": "250ml"})
        self.ord_lst.update({"Discount": float(input("""please enter the discount 
                            for the specified food: """))})
        print(self.ord_lst)
        self.menu1.update({self.id: self.ord_lst})
        self.id += 1
        print(self.menu1)

        with open("menu.txt", "a+") as menu_data:
            menu_data.write(json.dumps(self.menu1))
            menu_data.write("\n")

        data().show_menu()





    def rm_menu(self):
        trun=int(input("""please enter
        1 to remove 1 item at a time
        2 to clear all the menu
        """))
        if trun==1:
            with open(r"menu.txt", "r+") as menu_data:
                local1=menu_data.readlines()
                data().show_menu()
                menu_data.seek(0)
                menu_data.truncate()
                menu_data.writelines(local1[:int(input("enter index no"))-1])

        elif trun==2:
            with open("menu.txt", "r+") as menu_data:
                menu_data.readlines()
                menu_data.seek(0)
                menu_data.truncate(0)



