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
    origin = db.Column(db.Integer, nullable=False)
    road = db.Column(db.Integer, nullable=False)

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
        task.content = request.form['content']
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
    print("TUTAJ")

    points = Point.query.order_by(Point.name).all()

    print(points)
    API_KEY = "AIzaSyDbufDUZ5lW7lWJOrdYlrY9zPCSmHcEAMM"
    client = googlemaps.Client(API_KEY)

    for p in points:
        for destination in points:
            if p != destination:
                directions_result = client.directions(origin=p.coordinates,
                                                      destination=destination.coordinates,
                                                      mode="driving",
                                                      avoid="ferries")

                distance = directions_result[0]['legs'][0]['distance']
                road = Road(id=1, origin_id=p.id, destination_id=destination.id,
                            distance=distance['value']) #jedna  trasa pomiedzy p a distance w tabeli Road
    #CHANGE IT
    db.session.add(points)

    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

