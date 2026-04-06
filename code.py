# Room data
rooms = {
    "1B": {"available": 2, "price": 1500},
    "2B": {"available": 2, "price": 2000},
    "4B": {"available": 6, "price": 2500}
}

# Show available rooms
def show_rooms():
    print("\nAvailable Rooms:")
    for r in rooms:
        print(r, "- Available:", rooms[r]["available"], " Price:", rooms[r]["price"])

# Booking function
def book_room():
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    age = int(input("Enter Age: "))

    if age < 18:
        print("Booking not allowed (Age < 18)")
        return

    show_rooms()

    room_type = input("Select Room Type (1B / 2B / 4B): ")

    if room_type not in rooms:
        print("Invalid room type")
        return

    if rooms[room_type]["available"] <= 0:
        print("Room not available")
        return

    # Only number of days
    days = int(input("Enter number of days (1,2,3...): "))

    # Simple condition
    if days <= 0:
        print("Invalid number of days")
        return

    # Calculate total
    total = rooms[room_type]["price"] * days

    # Update availability
    rooms[room_type]["available"] -= 1

    # Output
    print("\n--- Booking Confirmed ---")
    print("Name:", name)
    print("Room Type:", room_type)
    print("Days:", days)
    print("Total Amount:", total)

# Main menu loop
while True:
    print("\n1. Show Rooms")
    print("2. Book Room")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")


