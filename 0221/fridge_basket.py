>>> fridge=['apple','banana','bread','juice']
>>> while fridge:
    eatery=fridge.pop(0)
    '냠냠'+eatery
    
'냠냠apple'
'냠냠banana'
'냠냠bread'
'냠냠juice'
>>> fridge
[]
>>> basket=['T-shirt','trousers','short','jacket']
>>> washing_machine=[]
>>> while basket:
    ot=basket.pop(0)
    washing_machine.append(ot)
    
>>> basket

[]
>>> washing_machine
['T-shirt', 'trousers', 'short', 'jacket']
>>> for ot in washing_machine:
    '세탁 ' + ot
    
'세탁 T-shirt'
'세탁 trousers'
'세탁 short'
'세탁 jacket'
>>> washing_machine
['T-shirt', 'trousers', 'short', 'jacket']
>>>
#예시 : 책장, 화장대, 술냉장고, 식기세척기, 오븐, 등등
