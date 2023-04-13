x1,x2=0.05,0.10

w1,w2=0.15,0.20
w3,w4=0.25,0.30
b1,b2=0.35,0.35

w5,w6=0.40,0.45
w7,w8=0.50,0.55
b3,b4=0.60,0.60

y1T,y2T=0.01,0.99

lr=0.01

for epoch in range(2000):
    
    h1=x1*w1+x2*w2+1*b1
    h2=x1*w3+x2*w4+1*b2
    
    y1=h1*w5+h2*w6+1*b3
    y2=h1*w7+h2*w8+1*b4
    
    E=((y1-y1T)**2+(y2-y2T)**2) / 2
    
    y1E=y1-y1T
    y2E=y2-y2T
    
    w5E=y1E*h1
    w6E=y1E*h2
    w7E=y2E*h1
    w8E=y2E*h2
    b3E=y1E*1
    b4E=y2E*1
    
    h1E=y1E*w5+y2E*w7
    h2E=y1E*w6+y2E*w8
    
    w1E=h1E*x1
    w2E=h1E*x2
    w3E=h2E*x1
    w4E=h2E*x2
    b1E=h1E*1
    b2E=h2E*1
    
    w5=w5-lr*w5E
    w6=w6-lr*w6E
    w7=w7-lr*w7E
    w8=w8-lr*w8E
    b3=b3-lr*b3E
    b4=b4-lr*b4E
    
    w1=w1-lr*w1E
    w2=w2-lr*w2E
    w3=w3-lr*w3E
    w4=w4-lr*w4E
    b1=b1-lr*b1E
    b2=b2-lr*b2E
    
    print(f'epoch={epoch}')
    print(f'y1:{y1:.3f}')
    print(f'y2:{y2:.3f}')
    
    if E<0.0000001:
        break