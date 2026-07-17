
class Hotel:
    def __init__(self, name: str, rooms_available: int, location: str, rating: int, price_per_room: float):
        self.name = name
        self.rooms_available = rooms_available
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room
    
    def __repr__(self) -> str:
        return (f"Hotel Name: {self.name} | "
                f"Rooms Available: {self.rooms_available} | "
                f"Location: {self.location} | "
                f"Rating: {self.rating}/5 | "
                f"Price/Room: ${self.price_per_room}")


class User:
    def __init__(self, name: str, user_id: int, booking_cost: float):
        self.name = name
        self.user_id = user_id
        self.booking_cost = booking_cost

    def __repr__(self) -> str:
        return f"User Name: {self.name} | User ID: {self.user_id} | Booking Cost: ${self.booking_cost}"


# --- Helper Input Functions with Validation ---

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer number.")

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid decimal number.")


# --- Operations ---

def print_hotel_data(hotels):
    print("\n--- CURRENT HOTEL INVENTORY ---")
    for hotel in hotels:
        print(hotel)
    print("-" * 30)

def sort_hotels_by_name(hotels):
    print("\n[Action] Sorting Hotels by Name Alphabetically:")
    hotels.sort(key=lambda h: h.name)
    print_hotel_data(hotels)

def sort_hotels_by_rating(hotels):
    print("\n[Action] Sorting Hotels by Rating (Highest First):")
    hotels.sort(key=lambda h: h.rating, reverse=True)
    print_hotel_data(hotels)

def print_hotels_by_city(hotels):
    city = input("\nEnter the city location to filter hotels: ").strip()
    print(f"\n[Action] Filtering Hotels for Location: '{city}'")
    hotels_by_loc = [h for h in hotels if h.location.lower() == city.lower()]
    
    if hotels_by_loc:
        print_hotel_data(hotels_by_loc)
    else:
        print(f"No hotels found in '{city}'.")

def sort_by_rooms_available(hotels):
    print("\n[Action] Sorting Hotels by Room Availability (Lowest First):")
    hotels.sort(key=lambda h: h.rooms_available)
    print_hotel_data(hotels)

def print_user_bookings(users, hotels):
    print("\n--- USER BOOKING MAPPINGS ---")
    # Using zip to map users to hotels. If collections vary in size, it matches up to the shortest list.
    for user, hotel in zip(users, hotels):
        print(f"{user}  --->  Assigned Hotel: {hotel.name}")
    print("-" * 30)


# --- Core System Loop ---

def hotel_management_system():
    print("========================================")
    print("Welcome to the Hotel Management System")
    print("========================================")
    
    hotels = []
    users = []

    # 1. Collect Hotel Data
    num_hotels = get_int_input("How many hotels would you like to add? ")
    for i in range(num_hotels):
        print(f"\n--- Enter Details for Hotel #{i + 1} ---")
        name = input("Hotel Name: ").strip()
        rooms = get_int_input("Rooms Available: ")
        location = input("Location/City: ").strip()
        
        while True:
            rating = get_int_input("Rating (1 to 5): ")
            if 1 <= rating <= 5:
                break
            print("❌ Rating must be between 1 and 5.")
            
        price = get_float_input("Price Per Room: ")
        
        hotels.append(Hotel(name, rooms, location, rating, price))

    # 2. Collect User Data
    num_users = get_int_input("\nHow many users would you like to add? ")
    for i in range(num_users):
        print(f"\n--- Enter Details for User #{i + 1} ---")
        name = input("User Name: ").strip()
        user_id = get_int_input("User ID: ")
        cost = get_float_input("Total Booking Cost: ")
        
        users.append(User(name, user_id, cost))

    # 3. Process and Run Features if data exists
    if not hotels:
        print("\nNo hotel data entered. Exiting operations.")
        return

    print_hotel_data(hotels)
    sort_hotels_by_name(hotels)
    sort_hotels_by_rating(hotels)
    sort_by_rooms_available(hotels)
    print_hotels_by_city(hotels)
    
    if users:
        print_user_bookings(users, hotels)


if __name__ == '__main__':
    hotel_management_system()