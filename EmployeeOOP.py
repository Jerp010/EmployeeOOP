from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulation

    @abstractmethod
    def show_info(self):
        pass

# Inheritance
class Employee(Person):
    def __init__(self, name, age, department):
        super().__init__(name)
        self.__age = age               # Encapsulation
        self._department = department  # Encapsulation

    # Polymorphism
    def show_info(self):
        print(f"Employee Name: {self._name}")
        print(f"Age: {self.__age}")
        print(f"Department: {self._department}")

    @classmethod
    def from_string(cls, emp_str):  # Class Method
        name, age, department = emp_str.split("-")
        return cls(name, int(age), department)

    @staticmethod
    def company_motto():  # Static Method
        return "Empowering employees to grow."

    def get_age(self):    # Instance Method
        return self.__age


def main():
    emp1 = Employee("Alice", 30, "HR")                # Main constructor
    emp2 = Employee.from_string("Bob-25-Sales")       # Alternate constructor

    emp1.show_info()  # Polymorphism
    print("---")
    emp2.show_info()  # Polymorphism

    print("Company Motto:", Employee.company_motto())  # Static Method
    print("Bob's Age:", emp2.get_age())                # Instance Method

    print("Is emp1 an instance of Person?", isinstance(emp1, Person))  # Inheritance check


if __name__ == "__main__":
    main()
