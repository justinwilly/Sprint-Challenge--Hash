#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trip_dict = {}
    # starts up a "route" that has a number empty slots equal to the length of the trip
    route = [None] * length

    # goes through all the tickets
    # adds an item in the trip_dict for each ticket
    # the item in trip_dict has a key, value of the ticket source and the ticket destination
    for t in tickets:
        trip_dict[t.source] = t.destination

    cur = 'NONE'
    # loops through a range equal to the length
    # gives each indice in the route a value equal to the source/destination of each ticket from the trip_dict
    # Fills the final spot with 'NONE' to represent the final destination has been met
    for i in range(length):
        print('origin', i, cur)
        route[i] = trip_dict.get(cur)
        cur = route[i]
        print('new cur', i, cur)


    return route
