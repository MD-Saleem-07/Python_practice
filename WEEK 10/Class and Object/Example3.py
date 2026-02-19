#example 3

class Mobile:
    def __init__(self):
        self.model='RealMe X'

    def show_model(self):
        print("Model:",self.model)

#creatring object of class
realme = Mobile()

#Accessing varibles from outside class

print (realme.model)

#Assign varibale a new value
realme.model ='RealMe pro2'

print (realme.model)

#Accessing method from outside class

realme.show_model()