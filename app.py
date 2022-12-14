
from flask import Flask, render_template

app = Flask(__name__)


#Using the below, the popup message appears on the page load of index.html
#0x00001000 - This makes the popup appear over the browser window
@app.route('/')
def index():
    return render_template('hello ça marche')

#Using the below, the popup message appears when the button is clicked on the webpage.
#0x00001000 - This makes the popup appear over the browser window
@app.route('/test')
def test():
    return render_template('hello ça marche')
@app.route('/test.html')
def test():
    return render_template('hello ça marche')

if __name__ == "__main__":
    app.run(debug=True)
