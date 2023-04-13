Python 3.10.9 (C:\Program Files (x86)\Thonny\python.exe)
>>> class CoffeeMachine:
    def __init__(self):
        self.menu={}
        self.total_money=0
    def set_menu(self, **menu):
        self.menu=menu
    def get_coffee(self, money_in, coffee_in):
        change, coffee_out=money_in, None
        if coffee_in in self.menu.keys():
            price=self.menu[coffee_in]
            if money_in>=price:
                change=money_in-price
                coffee_out=coffee_in
        return change, coffee_out
    
>>> cm=CoffeeMachine()
>>> menu={'americano':1500,'caffe latte':2500,'espresso':1500}
>>> cm.set_menu(**menu)
>>> print(cm.menu)
{'americano': 1500, 'caffe latte': 2500, 'espresso': 1500}
>>> change,coffee=cm.get_coffee(5000,'espresso')
>>> print(change, coffee)
3500 espresso
>>> 
