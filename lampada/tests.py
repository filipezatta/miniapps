class Student(object):
    def __init__(self, name, surname, age, grade, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade
        self.address = address

def create_student():
    name = input("Enter name")
    surname = input("Enter surname")
    age = input("Enter age")
    grade = input("Enter grade")
    address = input("Enter address")
    return Student(name, surname, age, grade, address)

number_of_students = int(input('How many students do you want to create? --> '))
students = []
for x in range(number_of_students):
    #create a student entering the infos
    students += [create_student()]
    
    """
    https://stackoverflow.com/questions/66644604/how-can-i-dynamically-create-an-object-of-a-class-in-python-3
    https://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname
    """