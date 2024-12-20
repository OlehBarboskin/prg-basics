class Phone():
    def __init__(self):
        self.turned_on = False
        self.turned_off = False
        self.sleep = False
    def turn_on (self):
        if self.turned_off == False and self.sleep == False:
            self.turned_on = True
    def turn_off (self):
        if self.turned_on == False and self.sleep == False:
            self.turned_off = True
    def slee (self):
        if self.turned_off == False and self.turned_on == False:
            self.sleep = True
Iphone124 = Phone()