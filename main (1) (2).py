# Flight Ticket Booking Program

class Flight:
    def __init__(self, flight_number, origin, destination, seats, price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.price = price

    def display_info(self):
        print(f"Flight: {self.flight_number}, Origin: {self.origin}, Destination: {self.destination}, "
              f"Seats Available: {self.seats}, Price per Ticket: ${self.price}")

class Booking:
    def __init__(self):
        self.available_flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.available_flights.append(flight)

    def display_flights(self):
        if not self.available_flights:
            print("No flights available.")
            return
        for i, flight in enumerate(self.available_flights, 1):
            print(f"{i}. ", end="")
            flight.display_info()

    def book_ticket(self, flight_number, passenger_name, seats_requested):
        flight = self.get_flight_by_number(flight_number)
        if flight:
            if flight.seats >= seats_requested:
                flight.seats -= seats_requested
                total_price = seats_requested * flight.price
                self.bookings.append({
                    'passenger': passenger_name,
                    'flight': flight.flight_number,
                    'seats': seats_requested,
                    'total_price': total_price
                })
                print(f"Booking confirmed for {passenger_name}: {seats_requested} seat(s) on flight {flight.flight_number}. "
                      f"Total cost: ${total_price}.")
            else:
                print(f"Not enough seats available on flight {flight_number}. Available seats: {flight.seats}.")
        else:
            print(f"Flight {flight_number} not found.")

    def get_flight_by_number(self, flight_number):
        for flight in self.available_flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def display_bookings(self):
        if not self.bookings:
            print("No bookings made yet.")
            return
        for booking in self.bookings:
            print(f"Passenger: {booking['passenger']}, Flight: {booking['flight']}, "
                  f"Seats: {booking['seats']}, Total Price: ${booking['total_price']}")

    def view_my_bookings(self, passenger_name):
        personal_bookings = [booking for booking in self.bookings if booking['passenger'] == passenger_name]
        if not personal_bookings:
            print(f"No bookings found for {passenger_name}.")
        else:
            print(f"Bookings for {passenger_name}:")
            for booking in personal_bookings:
                print(f"Flight: {booking['flight']}, Seats: {booking['seats']}, Total Price: ${booking['total_price']}")

    def cancel_ticket(self, passenger_name, flight_number):
        booking_to_cancel = None
        for booking in self.bookings:
            if booking['passenger'] == passenger_name and booking['flight'] == flight_number:
                booking_to_cancel = booking
                break

        if booking_to_cancel:
            self.bookings.remove(booking_to_cancel)
            flight = self.get_flight_by_number(flight_number)
            if flight:
                flight.seats += booking_to_cancel['seats']
            print(f"Booking for {passenger_name} on flight {flight_number} has been canceled.")
        else:
            print(f"No booking found for {passenger_name} on flight {flight_number}.")

# Sample usage
booking_system = Booking()

# Adding some flights
booking_system.add_flight(Flight("FL123", "New York", "London", 100, 500))
booking_system.add_flight(Flight("FL456", "Los Angeles", "Paris", 80, 650))
booking_system.add_flight(Flight("FL789", "Chicago", "Tokyo", 50, 800))

print("Welcome to the Flight Booking System")
while True:
    print("\nOptions:")
    print("1. View available flights")
    print("2. Book a flight")
    print("3. View all bookings")
    print("4. View my bookings")
    print("5. Cancel a booking")
    print("6. Exit")

    choice = input("Please choose an option: ")

    if choice == '1':
        print("\nAvailable Flights:")
        booking_system.display_flights()

    elif choice == '2':
        passenger_name = input("Enter passenger name: ")
        flight_number = input("Enter flight number: ")
        seats_requested = int(input("Enter number of seats to book: "))
        booking_system.book_ticket(flight_number, passenger_name, seats_requested)

    elif choice == '3':
        print("\nAll Booking Details:")
        booking_system.display_bookings()

    elif choice == '4':
        passenger_name = input("Enter passenger name to view your bookings: ")
        booking_system.view_my_bookings(passenger_name)

    elif choice == '5':
        passenger_name = input("Enter passenger name: ")
        flight_number = input("Enter flight number to cancel booking: ")
        booking_system.cancel_ticket(passenger_name, flight_number)

    elif choice == '6':
        print("Exiting the system. Thank you!")
        break

    else:
        print("Invalid option. Please try again.")
