"""
1. Object is created without exposing the logic to the client
2. For creating new type of object, the client uses same common interface

"""

from abc import ABC, abstractmethod

# factory method
def create_booking(booking_type):
    if booking_type == "movies":
        return Movies()
    elif booking_type == "liveshows":
        return LiveShows()

class Ticket(ABC):
    @abstractmethod
    def book(self):
        pass

class Movies(Ticket):
    def book(self):
        return f'Movies booking tickets'

class LiveShows(Ticket):
    def book(self):
        return f'Live Shows booking tickets'

def client_booking_app(booking_type):
    b = create_booking(booking_type)
    print(b.book())

if __name__=="__main__":
    client_booking_app("movies")
    client_booking_app("liveshows")