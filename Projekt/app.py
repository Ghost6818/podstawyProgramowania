from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import googlemaps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    coordinates = db.Column(db.String(200), nullable=False)

class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    point_o = db.Column(db.Integer, nullable=False)
    point_s = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        coordinates = request.form['coordinates']
        point = Point(name=name, coordinates=coordinates)

        db.session.add(point)
        db.session.commit()
        return redirect('/')
    else:
        #wyjmowanie z tabeli POINT wszystkich rekordów`
        points = Point.query.order_by(Point.name).all()
    return render_template("index.html", points=points)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    #wyjęcie jednego elementu
    task = Point.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form['content']
        task.coordinates = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task = Point.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('delete.html', task=task)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    points = Point.query.order_by(Point.name).all()  #wyjmowanie z tabeli POINT wszystkich rekordów`
    API_KEY = "AIzaSyDbufDUZ5lW7lWJOrdYlrY9zPCSmHcEAMM"
    client = googlemaps.Client(API_KEY)

    for p in points:
        for destination in points:
            if p != destination:
                directions_result = client.directions(origin=p.coordinates,
                                                      destination=destination.coordinates,
                                                      mode="driving",
                                                      avoid="ferries")

                print(p.name, 'do', destination.name, directions_result[0]['legs'][0]['distance']['text'])

                distance = directions_result[0]['legs'][0]['distance']
                road = Road(point_o=p.id, point_s=destination.id,
                            distance=distance['value'])   #jedna  trasa pomiedzy p a distance w tabeli Road


    def first(collection):
        return next(iter(collection))

    def distance(a, b):
        roads = set(Road.query.all())
        for r in roads:
            if a.id == r.origin and b.id == r.destination:
                return r.distance

    def nearest_neighbour(a, points, roads):
        return min(points, key=lambda c: distance(c, a,roads))

    def nn_tour(points):
        start = first(points)
        tour = [start] #dodawanie point
        unvisited = set(points - {start})
        while unvisited:
            c = nearest_neighbour(tour[-1], unvisited)
            tour.append(c)
            unvisited.remove(c)
        return tour

    db.session.add(road)
    db.session.commit()
    return render_template('calculate.html', points=points)

if __name__ == "__main__":
    app.run(debug=True)