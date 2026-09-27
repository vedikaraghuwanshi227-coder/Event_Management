from event import add_event, view_events
from registration import register_student, view_registrations

while True:
    print("\n===== EVENT MANAGEMENT SYSTEM =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Register Student")
    print("4. View Registrations")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        register_student()
    elif choice == "4":
        view_registrations()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
        