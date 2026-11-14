
# -----------------------------------------
# Python OOP Project: Employee Management System
# -----------------------------------------

# Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Employee Class (Base Class)
class Employee(Person):
    def __init__(self, name, age, employee_id=None, salary=0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter and setter for employee ID
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Display employee details
    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass


# Manager Class (Derived Class)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary,
                 department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        super().display()
        print("Department:", self.department)


# Developer Class (Derived Class)
class Developer(Employee):
    def __init__(self, name, age, employee_id, salary,
                 programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        super().display()
        print("Programming Language:",
              self.programming_language)


# -----------------------------------------
# Employee Management System
# -----------------------------------------

people = []
employees = []
managers = []
developers = []


while True:

    print("\n--- Python OOP Project: Employee Management System ---")

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Create Person
    if choice == "1":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        people.append(person)

        print("\nPerson created successfully!")
        print("Person created with name:", name,
              "and age:", age)

    # Create Employee
    elif choice == "2":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, employee_id, salary)
        employees.append(employee)

        print("\nEmployee created successfully!")
        print("Employee created with name:", name)
        print("Age:", age)
        print("ID:", employee_id)
        print("Salary:", salary)

    # Create Manager
    elif choice == "3":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, employee_id,
                          salary, department)

        managers.append(manager)

        print("\nManager created successfully!")
        print("Manager:", name)
        print("Department:", department)

    # Create Developer
    elif choice == "4":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(name, age, employee_id,
                              salary, language)

        developers.append(developer)

        print("\nDeveloper created successfully!")
        print("Developer:", name)
        print("Programming Language:", language)

    # Show Details
    elif choice == "5":

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        detail_choice = input("Enter your choice: ")

        if detail_choice == "1":
            if people:
                for person in people:
                    print("\nPerson Details:")
                    person.display()
            else:
                print("No person records found.")

        elif detail_choice == "2":
            if employees:
                for employee in employees:
                    print("\nEmployee Details:")
                    employee.display()
            else:
                print("No employee records found.")

        elif detail_choice == "3":
            if managers:
                for manager in managers:
                    manager.display()
            else:
                print("No manager records found.")

        elif detail_choice == "4":
            if developers:
                for developer in developers:
                    developer.display()
            else:
                print("No developer records found.")

        else:
            print("Invalid choice!")

    # Exit
    elif choice == "6":

        print("\nExiting the system.")
        print("All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")


# -----------------------------------------
# Checking Inheritance
# -----------------------------------------

print("\n--- Inheritance Checking ---")

print("Is Manager a subclass of Employee?",
      issubclass(Manager, Employee))

print("Is Developer a subclass of Employee?",
      issubclass(Developer, Employee))
