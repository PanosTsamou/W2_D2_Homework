class BusStop:

    #Initialise BusStop properties
    def __init__(self, input_busstop_name):
        self.name = input_busstop_name
        self.queue = [ ]

    #it returns the number of people waiting at the bus stop
    def queue_length(self):
        return len(self.queue)

    #adds peoples at the bus stop
    def add_to_queue(self, new_person):
        self.queue.append(new_person)

    # empties the bus stop
    def clear_queue(self):
        self.queue.clear()
    