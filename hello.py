from flask import Flask
app = Flask(__name__)

moje_imie = 'Natalia'

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto', methods=["POST"])
def kto():
    if request.method == 'POST':
        fname = request.form["fname"]
        lname = request.form["lnamec"]
    return 'Hello, World ' + fname + lname +'!'


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'
