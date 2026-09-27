# Student registration functions

from data import events, registrations
from validation import get_non_empty_input, get_event_choice
from event import view_events


def register_student():
    if not events:
        print("\nNo events available for registration.")
        return

    print("\n--- Student Registration ---")

    view_events()

    choice = get_event_choice(len(events))

    student = get_non_empty_input("Enter student name: ")
    roll = get_non_empty_input("Enter roll number: ")

    registration = {
        "student": student,
        "roll": roll,
        "event": events[choice - 1]["name"]
    }

    registrations.append(registration)

    print("\nRegistration successful!")


def view_registrations():
    if not registrations:
        print("\nNo registrations found.")
        return

    print("\n--- Student Registrations ---")

    for i, registration in enumerate(registrations, start=1):
        print(f"\nRegistration {i}")
        print("Student:", registration["student"])
        print("Roll No:", registration["roll"])
        print("Event:", registration["event"])
