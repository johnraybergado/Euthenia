from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/netherlands')
def netherlands():
    return render_template('netherlands.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/cereals')
def cereals():
    return render_template('cereals.html')

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')

@app.route('/meat')
def meat():
    return render_template('meat.html')

@app.route('/oilseeds')
def oilseeds():
    return render_template('oilseeds.html')

@app.route('/othercashcrops')
def othercashcrops():
    return render_template('othercashcrops.html')

@app.route('/roots')
def roots():
    return render_template('roots.html')

@app.route('/detailed/')
@app.route('/detailed/<country>')
def detailed(country=None):
	return render_template('detailed.html', country=country)

if __name__ == '__main__':
	app.debug = True
	app.run()