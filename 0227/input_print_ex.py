x1,x2,x3=0.02,0.05,0.12
y1T,y2T=0.02,0.98
w1,w2,w3,b1=0.15,0.20,0.02,0.12
w4,w5,w6,b2=0.27,0.37,0.52,0.39
lr = 0.01

for epoch in range(2000):
    
    y1 = x1*w1 + x2*w2 +x3*w3 + 1*b1
    y2 = x1*w3 + x2*w4 +x3*w6 + 1*b2
   
    
    E =((y1-y1T)**2 +(y2-y2T)**2) / 2
    
    y1E,y2E = y1 - y1T,y2-y2T
    
    w1E = y1E*x1; w2E = y1E*x2; w3E = y1E*x3; b1E = y1E*1
    w4E = y2E*x1; w5E = y2E*x2; w6E = y2E*x3; b2E = y2E*1
    
    w1 -= lr*w1E
    w2 -= lr*w2E
    b1 -= lr*b1E
    w3 -= lr*w3E
    w4 -= lr*w4E
    b2 -= lr*b2E
    w5 -= lr*w5E
    w6 -= lr*w6E
    
    
    print(f'epoch = {epoch}')
    print(f' y1 : {y1:.3f}')
    print(f' y2 : {y2:.3f}')
    print(f' w1 : {w1:.3f}')
    print(f' w2 : {w2:.3f}')
    print(f' b1 : {b1:.3f}')
    print(f' w3 : {w3:.3f}')
    print(f' w4 : {w4:.3f}')
    print(f' b2 : {b2:.3f}')
    print(f' w5 : {w5:.3f}')
    print(f' w6 : {w6:.3f}')
    
    if E < 0.000000001 :
        break

