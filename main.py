

class Hotel:
    def __init__(self, name: str, rooms_available: int, location: str, rating: int, price_per_room: float):
        self.name = name
        self.rooms_available = rooms_available
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room
    
    def __repr__(self) -> str:
        return (f"PRHOTELS DATA:\n"
                f"Hotel Name: {self.name}\t"
                f"Rooms Available: {self.rooms_available}\t"
                f"Location: {self.location}\t"
                f"Rating: {self.rating}\t"
                f"Price/Room: {self.price_per_room}")


class User:
    def __init__(self, name: str, user_id: int, booking_cost: float):
        self.name = name
        self.user_id = user_id
        self.booking_cost = booking_cost

    def __repr__(self) -> str:
        return f"User Name: {self.name}\tUser ID: {self.user_id}\tBooking Cost: {self.booking_cost}"


# --- Operations ---

def print_hotel_data(hotels):
    for hotel in hotels:
        print(hotel)
    print()

def sort_hotels_by_name(hotels):
    print("SORT BY NAME:")
    # Using Python's native key parameter for clean, in-place sorting
    hotels.sort(key=lambda h: h.name)
    print_hotel_data(hotels)

def sort_hotels_by_rating(hotels):
    print("SORT BY RATING:")
    hotels.sort(key=lambda h: h.rating, reverse=True) # Usually higher rating comes first
    print_hotel_data(hotels)

def print_hotels_by_city(city: str, hotels):
    print(f"HOTELS FOR {city.upper()} LOCATION ARE:")
    hotels_by_loc = [h for h in hotels if h.location.lower() == city.lower()]
    print_hotel_data(hotels_by_loc)

def sort_by_rooms_available(hotels):
    print("SORT BY ROOMS AVAILABLE:")
    hotels.sort(key=lambda h: h.rooms_available)
    print_hotel_data(hotels)

def print_user_bookings(users, hotels):
    print("USER BOOKING DETAILS:")
    for user, hotel in zip(users, hotels):
        print(f"{user} \tMapped Hotel: {hotel.name}")
    print()


def hotel_management_system():
    # Sample Dataset Initialization
    user_names = ["U1", "U2", "U3"]
    user_ids = [2, 3, 4] 
    booking_costs = [1000, 1200, 1100]

    hotel_names = ["H1", "H2", "H3"] 
    rooms = [4, 5, 6] 
    locations = ["Bangalore", "Bangalore", "Mumbai"]
    ratings = [5, 4, 3]
    prices = [100, 200, 100] 

    # Building object lists safely via zip mapping
    hotels = [
        Hotel(hotel_names[i], rooms[i], locations[i], ratings[i], prices[i])
        for i in range(len(hotel_names))
    ]
    
    users = [
        User(user_names[i], user_ids[i], booking_costs[i])
        for i in range(len(user_names))
    ]

    # Execute and display actions
    print("--- INITIAL HOTEL DATA ---")
    print_hotel_data(hotels)
    
    sort_hotels_by_name(hotels)
    sort_hotels_by_rating(hotels)
    print_hotels_by_city("Bangalore", hotels)
    sort_by_rooms_available(hotels)
    print_user_bookings(users, hotels)


if __name__ == '__main__':
    hotel_management_system()

