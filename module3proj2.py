our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def shared_flights():
    shared_flights = our_routes.intersection(competitor_routes)
    print(shared_flights)

shared_flights()    

def independent_flights():
    lone_routes = our_routes.difference(competitor_routes)
    print(lone_routes)

independent_flights()

def singular_flights_shared():
    alone_togehter_flights = our_routes.symmetric_difference(competitor_routes)
    print(competitor_routes)

singular_flights_shared()




#2

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

New_IDs = set(customer_ids)
print(New_IDs)