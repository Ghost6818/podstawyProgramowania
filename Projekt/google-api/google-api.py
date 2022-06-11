import googlemaps

API_KEY = "AIzaSyDbufDUZ5lW7lWJOrdYlrY9zPCSmHcEAMM"
client = googlemaps.Client(API_KEY)

#symulacja tabeli w bazie danych
class Point:
    def __init__(self, id,name, cordinates):
        self.id = id
        self.name = name
        self.cordinates = cordinates

class Road:
    def __init__(self, id, origin_id, destination_id, distance, road):
        self.id = id
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.distance = distance
        self.road = road

points = Point.query.order_by(Point.name).all()
#sumulacja wprowadzania punktów na stroe


# points = set(Point.query.all())
#funkcja obliczjąca krawędzie app

#OBLICZENIE OSTATECZNEJ KLASY (wyświetl na podstwronie calculate
#iter next obiekt (kolejny element z naszego zbioru iteruje
#pobranie pierwszego elementu i ustawienie jego jako startowy punkt
#obliczenie z wyłączeniem punktu startowego
#dopóki jest jeszcze jakiś nie odwiedzony
#bez ostatniego dodatengo punktu
#minimum z punktów a jako klucz = lambda pomiędzy naszym punktem c a punktem a liczymy dystans na podstawie dróg które mamy w bazie
#distane przejści po drogach i sprawdzenie
#dla naszego punktu C dystans jest najmniejszy
#zapisujemy punkt do naszej trasy usuwamy z punktów nie odwiedzonych
#wiec kolejny najbliższy punkt od ostatniego

def first(collection):
    return next(iter(collection))

def distance(a, b, roads):
    for r in roads:
        if a.id == r.origin and b.id == r.destination:
            return r.distance

def nearest_neighbour(a, points):
    return min(points, key=lambda c: distance(c, a, roads))

def nn_tour(points):
    start = first(points)
    tour = [start] #dodawanie point
    unvisited = set(points - {start})
    while unvisited:
        c = nearest_neighbour(tour[-1], unvisited)
        tour.append(c)
        unvisited.remove(c)
    return tour

for n in nn_tour(points): #przoechodzenie po liście punktów
    print(n.name)