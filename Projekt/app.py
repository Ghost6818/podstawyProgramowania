from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    coordinates = db.Column(db.Float, nullable=False)

class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    point_o = db.Column(db.Integer, nullable=False)
    point_s = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task = Point(content=task_content)

        db.session.add(task)
        db.session.commit()
        return redirect('/')
    else:
        tasks = Point.query.order_by(Point.name).all()
    return render_template("index.html", tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
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

if __name__ == "__main__":
    app.run(debug=True)

