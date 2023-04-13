>>> class Remote:
    def __init__(self,car):
        self.car=car
    def go_forward(self,spd):
        self.car.go_forward()
        self.car.set_speed(spd)
    def stop(self):
        self.car.stop()
    def show_screen(self):
        self.car.show_state()
        
>>> remote=Remote(mycar)
>>> remote.go_forward(30)
>>> remote.show_screen()
('forward', 30)
>>> remote.stop()
>>> remote.show_screen()
('stop', 0)