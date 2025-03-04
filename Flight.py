

class Flight:
    def __init__(self, capsity):
        self.capsity = capsity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seat():
            return False    
        self.passenger.append(name)
        return True
    def open_seat(self):
        return self.capsity - len(self.passenger) 
    
flight = Flight(4)


peaople = [ "CALI ", "FAARAH", "GEEDI", "HALIMA"]


for person in peaople:
    if flight.add_passenger(person):
        print(f"{person} has been added to the flight")
    else:
        print(f"no have space pls wait next flight Mr.{person}")