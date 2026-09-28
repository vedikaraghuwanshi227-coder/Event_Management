# College Event Management System

## Introduction

The College Event Management System is a simple Python-based application developed to manage college events and student registrations. The system uses a command-line interface (CLI) through which users can add events, view available events, register students, and view registrations.

## Features

* Add new college events
* View all available events
* Register students for events
* View student registrations
* Validate event selection
* Simple menu-driven interface

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* Exception Handling

## Project Structure

```text
College-Event-Management-System/
│
├── main.py
└── README.md
```

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/vedikaraghuwanshi227/Event_Management.git
```

### Step 2: Open the Project Directory

```bash
cd College-Event-Management-System
```

### Step 3: Run the Program

```bash
python main.py
```

## Application Menu

```text
==== College Event Management System ====

1. Add Event
2. View Events
3. Register Student
4. View Registrations
5. Exit
```

## Functionalities

### 1. Add Event

The user can add a new event by entering:

* Event name
* Event date
* Event venue

The event details are stored in the program.

### 2. View Events

This option displays all available events along with their date and venue.

### 3. Register Student

The user can select an event and register a student by providing:

* Student name
Roll number

The registration is then stored in the program.

4. View Registrations

This option displays all registered students along with their roll number and selected event.

5. Exit

This option terminates the program.

Data Storage

The current version uses Python lists and dictionaries to store event and registration data.

The data is stored temporarily in memory and will be lost when the program is closed.

Future Enhancements

The project can be further improved by adding:

Database integration using SQLite or MySQL
Admin and student login
Event editing and deletion
Duplicate registration prevention
Event capacity management
Search and filtering functionality
Graphical User Interface (GUI)
Conclusion

The College Event Management System provides a basic solution for managing college events and student registrations. It demonstrates fundamental Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, and exception handling.

Author

Vedika Raghuwanshi
