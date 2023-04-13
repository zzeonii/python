x = 2
w = 3
b = 1
yT = 10
lr = 0.01

for epoch in range(200):
    
    y = x*w + 1*b
    E = (y - yT)**2 / 2
    yE = y - yT
    wE = yE*x
    bE = yE*1
    w -= lr*wE
    b -= lr*bE
    
    print(f'epoch = {epoch}')
    print(f' y : {y:.3f}')
    print(f' w : {w:.3f}')
    print(f' b : {b:.3f}')
    
    if E < 0.0000001 :
        break
    