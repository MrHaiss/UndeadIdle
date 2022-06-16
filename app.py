from flask import Flask, render_template

app = Flask(__name__)

anguish_producers = {
    # The base mortal is the only one that produces anguish
    "Basic Mortal": {
        "ID": 0,
        "Cost-Anguish": 10,
        "Cost-Mortal": 1,
        "Cost-Prev": 0,
        "Production": 1
    },
    # All other tiers produce x of the previous tier, based off the ID
    "Advanced Mortal 1": {
        "ID": 1,
        "Cost-Anguish": 810,
        "Cost-Mortal": 1,
        "Cost-Prev": 100,
        "Production": 2
    },
    "Advanced Mortal 2": {
        "ID": 2,
        "Cost-Anguish": 72900,
        "Cost-Mortal": 1,
        "Cost-Prev": 1000,
        "Production": 3
    },
    "Advanced Mortal 3": {
        "ID": 3,
        "Cost-Anguish": 6560000,
        "Cost-Mortal": 1,
        "Cost-Prev": 10000,
        "Production": 4
    },
    "Advanced Mortal 4": {
        "ID": 4,
        "Cost-Anguish": 590000000,
        "Cost-Mortal": 1,
        "Cost-Prev": 100000,
        "Production": 5
    },
    "Advanced Mortal 5": {
        "ID": 5,
        "Cost-Anguish": 53100000000,
        "Cost-Mortal": 1,
        "Cost-Prev": 1000000,
        "Production": 6
    },
    "Advanced Mortal 6": {
        "ID": 6,
        "Cost-Anguish": 4780000000000,
        "Cost-Mortal": 1,
        "Cost-Prev": 10000000,
        "Production": 7
    }
}


@app.route("/")
def main_page():
    return render_template("landing_page.html", anguish_producers=anguish_producers)


app.run(debug=True)
