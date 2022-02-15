class Car(object):
    def __init__ (self,color,model,company,speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("I started My car")

    def stop(self):
        print("I stopped my car")

    def accelerate(self):
        print("I accelerated my car")

    def gear_change(self,gear_type):
        print("Gear "+ gear_type+" has been changed")

car1 = Car("red","A6","Audi", 220)
print(car1.gear_change("2"))