class Hotel:
    def __init__(self):
        self.__rooms = 10
    def book_room(self):
        if self.__rooms > 0:
            self.__rooms -= 1
            print("Room Booked")
        else:
            print("No Rooms Available")
    def show_rooms(self):
        print("Available Rooms:", self.__rooms)
hotel = Hotel()
hotel.book_room()
hotel.show_rooms()