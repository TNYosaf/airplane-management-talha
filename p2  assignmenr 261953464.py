# Create a dictionary to store flight information with seat layout
flights = {
    "Flight Company A": {
        "layout": [
            ["", "", "C"],
            ["", "", "*"],
            ["X", "X", "X"],
        ],
        "bookings": [],
    },
    "Flight Company B": {
        "layout": [
            ["*", "A", "B"],
            ["X", "*", "C"],
            ["D", "*", "E"],
        ],
        "bookings": [],
    },
}

# Function to display available flights
def display_flights():
    print("Available Flights:")
    for i, flight in enumerate(flights.keys(), start=1):
        print(f"{i}. {flight}")

# Function to book a seat
def book_seat(flight, row, seat):
    if flight in flights:
        layout = flights[flight]["layout"]
        bookings = flights[flight]["bookings"]
        if row < 1 or row > len(layout) or seat < 0 or seat >= len(layout[0]):
            return "Invalid row or seat."
        if layout[row - 1][seat] == "*":
            layout[row - 1][seat] = "X"
            bookings.append((row, seat))
            with open("booking_confirmation.txt", "a") as file:
                file.write(f"Flight: {flight}, Row {row} Seat {chr(ord('A') + seat)}.\n")
            return f"Seat {chr(ord('A') + seat)} in Row {row} has been successfully booked!"
        else:
            return "Seat already booked."
    else:
        return "Flight not found."

# Function to cancel a booking
def cancel_booking(flight, row, seat):
    if flight in flights:
        layout = flights[flight]["layout"]
        bookings = flights[flight]["bookings"]
        if row < 1 or row > len(layout) or seat < 0 or seat >= len(layout[0]):
            return "Invalid row or seat."
        if (row, seat) in bookings:
            layout[row - 1][seat] = "*"
            bookings.remove((row, seat))
            with open("cancellation_confirmation.txt", "a") as file:
                file.write(f"Flight: {flight}, Row {row} Seat {chr(ord('A') + seat)} has been canceled.\n")
            return f"Seat {chr(ord('A') + seat)} in Row {row} has been successfully canceled!"
        else:
            return "Seat not booked."
    else:
        return "Flight not found."

# Function to display all flights and their seat layouts
def show_all_flights():
    for flight, data in flights.items():
        layout = data["layout"]
        print(f"Flight: {flight} - Seat Layout:")
        for i, row in enumerate(layout, start=1):
            print(f"Row {i}:", " ".join(row))

# Main loop
while True:
    print("\nOptions:")
    print("1. Display Available Flights")
    print("2. Book a Seat")
    print("3. Cancel Booking")
    print("4. Show All Flights")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_flights()
    elif choice == "2":
        flight_choice = int(input("Choose a flight (enter the corresponding number): "))
        flight_name = list(flights.keys())[flight_choice]
        show_all_flights()
        row = int(input("Enter the row number: "))
        seat = ord(input("Enter the seat letter (A, B, C, etc.): ").upper()) - ord('A')
        print(book_seat(flight_name, row, seat))
    elif choice == "3":
        flight_choice = int(input("Choose a flight (enter the corresponding number): "))
        flight_name = list(flights.keys())[flight_choice - 1]
        show_all_flights()
        row = int(input("Enter the row number: "))
        seat = ord(input("Enter the seat letter (A, B, C, etc.): ").upper()) - ord('A')
        print(cancel_booking(flight_name, row, seat))
    elif choice == "4":
        show_all_flights()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")
