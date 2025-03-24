'''class Person:
    
    amount = 0
    
    def __init__(self, name, age, address):
        self.name = name 
        self.age = age
        self.address = address
        Person.amount += 1
        
    def __del__(self):
        Person.amount -= 1
        
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.address)
    
    def get_older(years):
        self.age += years
        

person1 = Person("John", 25, "New York")
print("person1")'''



class Vehicle:
    def __init__(self, model, engine):
        self.model  = model
        self.engine = engine
        
    def __str__(self):
        return "Model: {}, Engine: {},".format(self.model, self.engine)
    
    def big_engine(size):
        def big_engine(self, size):
            self.engine += size

# Person Class & Inheritance      
class Audi(Vehicle):
    def __init__(self, model, engine, cost):
        super(Audi, self).__init__(model, engine)
        self.cost = cost
        
    def __str__(self):
        text = super(Audi, self).__str__()
        text += ", Salary {}".format(self.cost)
        return text
        
    def yearly_cost(self):
        return self.cost * 12
    
Audi1 = Audi("E-Tron", "v8", 80000)
print(Audi1)
print(Audi1.yearly_cost())        