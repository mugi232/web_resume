from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/elements_theme')
def elements_theme():
    return render_template("elements.html")

# Run the web app

if __name__ == '__main__':
    app.run()
