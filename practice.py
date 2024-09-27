class Person:
    def __init__(self,name,city):
        self.name= name
        self.city= city

    def view(self):
        print(self.name)
        print(self.city)

p= Person("Abhay","Bhopal")
p.view()