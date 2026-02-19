#Example 4

class Mobile:
    def __init__(self):
        self.model='RealMe X'
    
    def show_model(self):
        price=1000     #Local variable
        print("Model:",self.model ,"and Price:",price)

realme = Mobile()

#Accessing method from outside class
realme.show_model()
