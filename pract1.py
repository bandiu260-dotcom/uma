class Student:

    def __init__(self, name=None, roll_no=None, branch=None):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def study(self):
        print(self.name, "is studying Python")


student1 = Student()
student1.name = "Ravi"
student1.roll_no = "11"
student1.branch = "CSD"

print(student1.name)
print(student1.roll_no)
print(student1.branch)
student1.study() 


class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 90

student = Student("Ravi")
print(student.name)

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(self.brand, self.model, "is starting")

    def stop(self):
        print(self.brand, self.model, "has stopped")

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)



car1 = Car("Toyota", "Innova", "White")


car1.display()


car1.start()
car1.stop()

class ATM:
    def withdraw(self):
        self.__check_pin()
        self.__check_balance()
        self.__dispense_cash()
        print("Withdrawal successful!")

    def __check_pin(self):
        print("Checking PIN...")

    def __check_balance(self):
        print("Checking balance...")

    def __dispense_cash(self):
        print("Dispensing cash...")


# Create an object and call the method
atm = ATM()
atm.withdraw()
