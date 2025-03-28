﻿Assignment1: Total 100
 
Question 1:
Create a simple class hierarchy involving a Vehicle class as the base class and two subclasses Car and Bike. Show how you would implement a method in the base class and override it in the subclasses.

Question 2:
Write a function that takes a list of different shapes (such as Circle and Rectangle) and calculates the total area of all shapes using polymorphism.

Question 3:
Scenario: You have a base class Shape with a method calculate_area(). You then create a derived class Rectangle that inherits from Shape. The Rectangle class needs to implement its own calculate_area() method, but you also want to utilize some initialization logic from the Shape class's constructor.

Demonstrate how to use the super() function within the Rectangle class's calculate_area() method (even if the shape class area method does nothing) to call the Shape class's constructor (__init__).

Question 4:
Scenario: You have a function process_sound(sound_object) that expects an object with a make_sound() method. You have two classes, Dog and Cat, both of which implement the make_sound() method, but in different ways.
Provide example code demonstrating how the process_sound() function can work with both Dog and Cat objects without needing to know their specific types.

Question 5:
Scenario: You are designing a system for handling different types of files. You want to ensure that all file handler classes implement certain essential methods, such as read() and write().
Provide example code demonstrating how to create an ABC FileHandler with abstract methods read() and write(), and how to create concrete classes like TextFileHandler and BinaryFileHandler that inherit from FileHandler.
