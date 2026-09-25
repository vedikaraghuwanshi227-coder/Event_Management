events = []
registrations = []


def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    venue = input("Enter venue: ")

    events.append({
        "name": name,
        "date": date,
        "venue": venue
    })

    print("Event added successfully.")


def view_events():
    if not events:
        print("No events available.")
        return

    print("\n--- College Events ---")

    for i, event in enumerate(events, 1):
        print(i, event["name"], "|", event["date"], "|", event["venue"])


def register_student():
    if not events:
        print("No events available.")
        return

    view_events()

    try:
        choice = int(input("Select event number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= choice <= len(events):
        student = input("Enter student name: ")
        roll = input("Enter roll number: ")

        registrations.append({
            "student": student,
            "roll": roll,
            "event": events[choice - 1]["name"]
        })

        print("Registration successful.")
    else:
        print("Invalid event number.")


def view_registrations():
    if not registrations:
        print("No registrations found.")
        return

    print("\n--- Registrations ---")

    for r in registrations:
        print(
            "Student:", r["student"],
            "| Roll No:", r["roll"],
            "| Event:", r["event"]
        )


while True:
    print("\n==== College Event Management System ====")
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
