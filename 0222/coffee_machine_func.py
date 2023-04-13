#함수와 커피 자판기
>>> menu={'americano':1500,'cafe latte':2500,'espresso':1500} #dict
>>> total_money=0
>>> def coffee_machine(money, coffee_in): #함수
    change, coffee_out=money, None
    if coffee_in in menu.keys():
        value = menu[coffee_in]
        if money>=value:
            change=money - value
            coffee_out=coffee_in
        return change,coffee_out
    
>>> change, coffee=coffee_machine(5000,'americano')
>>> print(change,coffee)
3500 americano