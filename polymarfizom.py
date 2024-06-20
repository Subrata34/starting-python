class vehicle :
    def __init__(self,Model,brand,Equipment) :
        self.Model=Model
        self.brand=brand
        self.Equipment=Equipment

class plane(vehicle):
    pass

class car(vehicle):
    pass

c1=car("tt1","p11233","899944")
p1=plane("bmw","ec1223","thro56")
print(p1.brand,p1.Equipment,p1.Model)
print(c1.brand,c1.Equipment,c1.Model)