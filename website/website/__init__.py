from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/detailed/')
@app.route('/detailed/<country>')
def detailed(country=None):
	if country == "Netherlands":
		return render_template('netherlands.html', country=country)
	return render_template('detailed.html', country=country)

if __name__ == '__main__':
	app.debug = True
	app.run()