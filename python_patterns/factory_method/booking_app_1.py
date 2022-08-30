"""
The Factory method defines a method, which should be used for creating object. Subclass overrides this method
and decides which class of object will be created.

The return type of factory method is abstract class

New Ticket booking like Games can be introduced which breaking existing client code

"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Booking(ABC): 
    """
    The Booking class declares the factory method that returns an object of a Ticket class
    """     
    # factory method
    @abstractmethod
    def create_booking(self) -> Ticket:
        pass
    
    def book_ticket(self):
        # Call the create_booking to create a Ticket object
        ticket = self.create_booking()
        # Use ticket object to book the ticket
        result = ticket.book()
        return result
    
class MoviesBooking(Booking):
    """
    Signature of this method uses abstract Ticket class, even though it returns concrete Movies class.
    This ensures Booking is independent of concrete Movies class.
    """
    def create_booking(self) -> Ticket:
        return Movies()

class LiveShowsBooking(Booking):
    """
    Signature of this method uses abstract Ticket class, even though it returns concrete LiveShows class.
    This ensures Booking is independent of concrete LiveShows class.
    """
    def create_booking(self) -> Ticket:
        return LiveShows()

class Ticket(ABC):
    """
    Ticket defines the methods that all concrete class must implement.
    """
    @abstractmethod
    def book(self):
        pass

class Movies(Ticket):
    def book(self):
        return f'Movies booking tickets'

class LiveShows(Ticket):
    def book(self):
        return f'Live Shows booking tickets'

def client_booking_app(booking: Booking):
    print(booking.book_ticket())

if __name__ == "__main__":
    client_booking_app(MoviesBooking())
    client_booking_app(LiveShowsBooking())
