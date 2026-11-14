Employee Management System – Python OOP Project

1. Project Overview

The Employee Management System is a simple Python project developed using Object-Oriented Programming (OOP) concepts.

This project allows users to create and manage different types of people, employees, managers, and developers through a menu-driven console interface.

It demonstrates important Python OOP concepts such as inheritance, encapsulation, method overriding, constructors, and polymorphism.

2. Project Objectives

To understand and implement Object-Oriented Programming in Python.

To create classes and objects.

To demonstrate inheritance between classes.

To protect sensitive information using encapsulation.

To implement method overriding.

To create an interactive menu-driven program.

3. Technologies Used

Programming Language: Python 3

Concept: Object-Oriented Programming (OOP)

Interface: Console-based User Interface

Editor: VS Code / Python IDLE

4. Class Structure

The project contains the following classes:

Person Class

Stores the person's name and age.

Contains a constructor to initialize attributes.

Contains a display method to show personal details.

Employee Class

Inherits from the Person class.

Stores employee ID and salary.

Uses private attributes for data protection.

Provides getter and setter methods.

Overrides the display method.

Manager Class

Inherits from the Employee class.

Contains an additional department attribute.

Overrides the display method to show manager information.

Developer Class

Inherits from the Employee class.

Contains an additional programming language attribute.

Overrides the display method to show developer information.

5. OOP Concepts Implemented

The following Object-Oriented Programming concepts are used:

Inheritance: Manager and Developer inherit properties and methods from Employee.

Encapsulation: Employee ID and salary are stored as private attributes.

Method Overriding: Child classes provide their own display methods.

Constructors: The __init__() method initializes objects.

Destructor: The __del__() method is defined in the Employee class.

super(): Used to access the parent class constructor and methods.

issubclass(): Used to check inheritance relationships.

Constructor Overloading: Default arguments allow different ways of creating Employee objects.

6. Main Features

The program provides the following menu options:

Create a Person

Create an Employee

Create a Manager

Create a Developer

Show Details

Exit
