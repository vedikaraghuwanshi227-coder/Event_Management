def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_event_choice(total_events):
    while True:
        try:
            choice = int(input("Enter event number: "))

            if 1 <= choice <= total_events:
                return choice

            print("Please enter a valid event number.")

        except ValueError:
            print("Please enter a number.")