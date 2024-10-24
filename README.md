# Library-System-Simulation
# Overview
This project simulates a library system using Python's threading capabilities. Multiple readers can borrow and return books from various libraries, demonstrating the principles of concurrent programming and resource management.

# Features
# Multiple Libraries: 
The simulation creates a specified number of libraries, each containing a set of books.
# Threading: 
Each reader operates in their own thread, allowing simultaneous borrowing and returning of books.
# Mutex Locking:
A locking mechanism ensures that only one thread can modify the library's book state at a time, preventing race conditions.
# Dynamic Book Management: 
Libraries can add and remove books dynamically during the simulation.

# Classes
Biblioteca: Represents a library that holds books. It includes methods to add, remove, and check the status of books.
Libro: Represents a book with attributes such as title, publisher, and publication date.
Lector: A thread that simulates a reader who borrows and returns books from the libraries.

# Skills Demonstrated

# Python Programming:
Proficient in Python and its libraries for threading and data manipulation.
# Concurrency and Threading: 
Understanding of multithreading and synchronization mechanisms (mutex locks).
# Object-Oriented Programming (OOP):
Implementation of classes and objects to model real-world entities.
# Data Structures: 
Use of dictionaries and lists to manage and organize data effectively.
# Problem Solving:
Ability to design a solution to simulate real-world scenarios and manage shared resources.
# Basic Debugging:
Identifying and resolving potential issues in concurrent programming, such as race conditions.
