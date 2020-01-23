from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/airfare/')
def airfare():
    return render_template('airfare.html')

@app.route('/real_estate/')
def real_estate():
    return render_template('real_estate.html')

@app.route('/<name>')
def dynamic(name):
    return '<h1>Something went wrong... add link to home page</h1>'


if __name__ == '__main__':
    app.run(debug=True)