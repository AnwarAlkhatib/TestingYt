from random  import randint

def add(a, b):
    return a + b

def devide(a, b):
    return a / b

def play_random():
    num = randint(0, 10)
    if num > 5:
        return "großer"
    return "Kleiner"


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    
    def something(self, a, b, c):
        pass