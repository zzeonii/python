###
>>> way_to_go=400*1000
>>> number_to_step=way_to_go*2.5
>>> step=0
>>> while step<number_to_step:
    step+=1
    
>>> step
1000000
###100만보가 될 때까지 2만보씩 알려줘
>>> step=0
>>> while step<number_to_step:
    step+=1
    if step%20000==0:
        print(step,'보')

###
>>> way_to_go=400*1000
>>> number_to_step=way_to_go*2.5
>>> step=0
>>> while True:
    step+=1
    if step>=number_to_step:
        break
    
>>> step
1000000       
