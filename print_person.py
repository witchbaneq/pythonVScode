from class_person import Person
# Это созадет экземпляр класса Person и вызывает метод print_person_info для каждого экземпляра.

class PrintPerson:
    person_one = Person("John",30, "USA", "male")
    person_two = Person("Alice", 25, "UK", "female")

    def print_person_info(person):
        print(person.name, person.age, person.country, person.gender) 
        return person

    print_person_info(person_one)
    print_person_info(person_two)