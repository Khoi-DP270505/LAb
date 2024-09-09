class Lunch:
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice:",self.menu, "Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:",self.menu, "Price 13.40")
        else:
            print("Error in menu")
lunch1 = Lunch("menu 1")
lunch1.menu_price()

lunch2 = Lunch("menu 2")
lunch2.menu_price()

lunch3 = Lunch("menu 3")
lunch3.menu_price()