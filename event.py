from data import events
from validation import get_non_empty_input


def add_event():
    print("\n--- Add New Event ---")

    name = get_non_empty_input("Enter event name: ")
    date = get_non_empty_input("Enter event date: ")
    venue = get_non_empty_input("Enter venue: ")

    event = {
        "name": name,
        "date": date,
        "venue": venue
    }

    events.append(event)

    print("\nEvent added successfully!")


def view_events():
    if not events:
        print("\nNo events available.")
        return

    print("\n--- College Events ---")

    for i, event in enumerate(events, start=1):
        print(
            f"{i}. {event['name']} | "
            f"Date: {event['date']} | "
            f"Venue: {event['venue']}"
        )


add_event()
view_events()