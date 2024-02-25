from datetime import datetime
class Airline:
    def __init__(self, airline_name, airline_code):
        self.airline_name = airline_name
        self.airline_code = airline_code

    def get_airline_info(self):
        # This method will return the details of the airline
        print(f"Airline Name: {self.airline_name}, Airline Code: {self.airline_code}")

class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, origin, destination):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination

    def get_flight_info(self):
        # this method will return the details about the flight
        print(f"Flight Number: {self.flight_number}, Departure Time: {self.departure_time}, "
              f"Arrival Time: {self.arrival_time}, Origin: {self.origin}, Destination: {self.destination}")

class Passenger:
    def __init__(self, passenger_id, name, email):
        self.passenger_id = passenger_id
        self.name = name
        self.email = email

    def get_details(self):
        # And this method will return the details of the passenger
        print(f"Passenger ID: {self.passenger_id}, Name: {self.name}, Email: {self.email}")

class BoardingPass:
    def __init__(self, boarding_pass_id, passenger, flight, seat_number, gate, boarding_time):
        self.boarding_pass_id = boarding_pass_id
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number
        self.gate = gate
        self.boarding_time = boarding_time

    def get_boarding_pass_details(self):
        # This method withh return the details of the boarding pass
        print(f"Boarding Pass ID: {self.boarding_pass_id}, Seat Number: {self.seat_number}, "
              f"Gate: {self.gate}, Boarding Time: {self.boarding_time}")
        self.passenger.get_details()
        self.flight.get_flight_info()

# Example
airline = Airline("Etihad Airways", "EA")
flight = Flight("EA357", datetime.now(), datetime.now(), "Abu Dhabi", "Germany")
passenger = Passenger(1, "Fatima", "Fatimaal@gmail.com")
boarding_pass = BoardingPass(204, passenger, flight, "15B", "F6", datetime.now())


print(airline.get_airline_info())
print(flight.get_flight_info())
print(passenger.get_details())
print(boarding_pass.get_boarding_pass_details())
