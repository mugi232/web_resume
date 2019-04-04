from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/elements_theme')
def elements_theme():
    return render_template("elements.html")

@app.route('/marketplace')
def marketplace():
    return render_template("project-marketplace-details.html")

@app.route('/logistics')
def logistics():
    return render_template("project-logistics-details.html")

@app.route('/scrapper')
def scrapper():
    return render_template("project-scrapper-details.html")

# Run the web app

if __name__ == '__main__':
    app.run()
