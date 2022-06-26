class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

deyan=person("Deyan",40,"Male")
print (deyan.name)
print(deyan.age)
print(deyan.gender)

petar=person("Petar",40)
print (deyan.name)
print(deyan.age)


class animal(person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
