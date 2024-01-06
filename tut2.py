from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def harry():
    nme = "harry"
    return render_template('about.html', name = '')

@app.route("/new")
def demo():
    n1 = 10
    n2 = 20


@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run()