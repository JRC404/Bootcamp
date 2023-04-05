class Person:
    def __init__(self, fullName, age, location, legs):
        self.fullName = fullName
        self.age = age
        self.location = location
        self.legs = legs
        self.employer = "Lloyds Banking Group"

terry = Person("Terry Khul", 28, "North London", 2)
print(terry.fullName)