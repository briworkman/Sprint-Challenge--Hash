#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trips = {}
    routes = []
    index = 0
    destination = "NONE"

    for i in tickets:
        # TODO: set the starting location as the key and the destination as its value
        trips[i.source] = i.destination

    while index < length:
        # TODO: set the current destination as the new source of the next ticket
        destination = trips.get(destination)
        routes.append(destination)
        index += 1

    return routes
