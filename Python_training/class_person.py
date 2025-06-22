class Person: 
    def __init__(self, name, age, country, gender, car_color = None): # Constructor
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.car_color = car_color

    def say_name(self, last_name):
        print(f"Hello {self.name} {last_name}.")