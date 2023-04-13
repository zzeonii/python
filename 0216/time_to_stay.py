time_to_stay=8*60*60
tick=0
while tick<time_to_stay:
    if tick%100==0:
        print('study in 연희학교')
    tick+=1
    if tick%100==0:
        print(tick)

print('go home')
print('복습')
