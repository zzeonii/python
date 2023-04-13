# 1
>>> shopping={'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
>>> basket=[]
>>> for fruit, how_many in shopping.items():
    fruit,how_many
    plastic_bag=[]
    for _ in range(how_many):
        plastic_bag.append(fruit)
    basket.append(plastic_bag)
    
('apple', 3)
('pear', 2)
('hanrabong', 5)
('pine apple', 2)
>>> basket

[['apple', 'apple', 'apple'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple']]
>>>
# 2
>>> shopping={'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
>>> basket=[]
>>> for fruit, how_many in shopping.items():
    fruit,how_many
    basket.append([fruit]*how_many)
    
('apple', 3)
('pear', 2)
('hanrabong', 5)
('pine apple', 2)
>>> basket
[['apple', 'apple', 'apple'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple']]
# 3(리스트 내포)
>>> shopping={'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
>>> basket=[[fruit]*how_many for fruit, how_many in shopping.items()]
>>> basket[['apple', 'apple', 'apple'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple']]
# 4(while문)
>>> shopping={'apple': 3, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
>>> basket=[]
>>> while shopping:
    fruit,how_many=shopping.popitem()
    fruit,how_many
    basket.append([fruit]*how_many)
    
('pine apple', 2)
('hanrabong', 5)
('pear', 2)
('apple', 3)
>>> shopping
{}
>>> basket
[['pine apple', 'pine apple'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pear', 'pear'], ['apple', 'apple', 'apple']]