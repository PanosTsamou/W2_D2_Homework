class Bus:

    #Initialise the Bus properties
    def __init__(self, input_route_num, input_bus_destination):
        self.route_number = input_route_num 
        self.destination = input_bus_destination
        self.passengers = []
        

    # return Brum brum string
    def drive(self):
        return "Brum brum"

    #adds passengers on the bus 
    def pick_up(self, picked_up_person):
        self.passengers.append(picked_up_person)

    #counts all bus passengers
    def passenger_count(self):
        return len(self.passengers)

    # drop off a passenger from the bus
    def drop_off(self, drop_off_person):
        self.passengers.remove(drop_off_person)

    # drop off all passengers from the bus
    def empty_bus(self):
        self.passengers = [ ]

    # pick up passengers from the bus stop
    def pick_up_from_stop(self, bus_stop_input):
        self.passengers.extend(bus_stop_input.queue)

    
    
    


