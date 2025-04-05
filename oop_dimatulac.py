class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")


class SchoolBus(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity} students")


# Task 2: Employee Class with Multiple Constructors
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

    @classmethod
    def default_employee(cls):
        return cls("John Doe", 30000)

    def display(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")


# Task 3: Two Schools with GPA
class SchoolOne:
    def __init__(self, students):
        self.students = students

    def average_gpa(self):
        return sum(self.students.values()) / len(self.students)

    def display(self):
        print("SchoolOne Students:")
        for name, grade in self.students.items():
            print(f"{name}: {grade}")
        print("Average GPA:", self.average_gpa())


class SchoolTwo:
    def __init__(self, students):
        self.students = students

    def average_gpa(self):
        return sum(self.students.values()) / len(self.students)

    def display(self):
        print("SchoolTwo Students:")
        for name, grade in self.students.items():
            print(f"{name}: {grade}")
        print("Average GPA:", self.average_gpa())


# Task 4: Vector Class with Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Task 5: Composition Over Inheritance
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: {self.title}")
        self.author.display()


if __name__ == "__main__":
    print("--- Vehicle and SchoolBus ---")
    bus = SchoolBus("Ford", "Transit", 50)
    bus.display_info()
    print("Is bus an instance of Vehicle?", isinstance(bus, Vehicle))

    print("\n--- Employee Constructors ---")
    emp1 = Employee("Alice", 40000)
    emp2 = Employee.from_string("Bob-50000")
    emp3 = Employee.default_employee()
    emp1.display()
    emp2.display()
    emp3.display()

    print("\n--- Schools and GPA ---")
    school1 = SchoolOne({"Alice": 3.5, "Bob": 3.8})
    school2 = SchoolTwo({"Charlie": 3.2, "David": 3.6})
    school1.display()
    school2.display()

    print("\n--- Vector Addition ---")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(v1)
    print(v2)
    print("Result of addition:", v3)

    print("\n--- Composition: Book and Author ---")
    author = Author("George Orwell", "British")
    book = Book("1984", author)
    book.display()
