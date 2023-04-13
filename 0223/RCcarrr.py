class RCCar:
    def __init__(self):
        self.dir='stop'
        self.spd=0
    def go_forward(self):
        self.dir='forward'
    def go_backward(self):
        self.dir='backward'
    def turn_left(self):
        self.dir='left'
    def turn_right(self):
        self.dir='right'
    def set_speed(self, spd):
        self.spd=spd
    def stop(self):
        self.dir='stop'
        self.spd=0
    def show_state(self):
        self.dir, self.spd
        
mycar=RCCar()
mycar.go_forward()
mycar.set_speed(30)
mycar.show_state()

('forward', 30)

