from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/day_1')
def day_1():
    return render_template('day-1.html')

if __name__ == '__main__':
    app.run(debug=True)
