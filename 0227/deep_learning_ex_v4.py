x1, x2 = 2, 3
w1, w2 = 3, 4
b = 1
yT = 27
lr = 0.01

for epoch in range(200):
    
    y = x1*w1 + x2*w2 + 1*b
    E = (y - yT)**2 / 2
    yE = y - yT
    w1E = yE*x1
    w2E = yE*x2
    bE = yE*1
    w1 -= lr*w1E
    w2 -= lr*w2E
    b = b - lr*bE
    
    print(f'epoch = {epoch}')
    print(f' y : {y:.3f}')
    print(f' w1 : {w1:.3f}')
    print(f' w2 : {w2:.3f}')
    print(f' b : {b:.3f}')
    
    if E < 0.0000001 :
        break
