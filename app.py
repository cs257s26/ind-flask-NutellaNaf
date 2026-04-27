from flask import Flask, request, redirect, url_for, abort
import dotenv
from ProductionCode.command_line import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return "Please look at the README.md to learn what routes to go to!"

@app.route('/<string:column_of_interest>')
def top_5_columns(column_of_interest):
    try:
        return_string = """"""
        results = nafees_user_story(column_of_interest)
        for result in results:
            return_string += "<p> " + str(result[0]) + f" in row {result[1]} </p>"
        return return_string
    
    except ValueError:
        return abort(404)

@app.route('/<int:n>/<string:column_of_interest>')
def top_n_columns(column_of_interest, n):
    try:
        return_string = """"""
        results = top_n_column_values(column_of_interest, n)
        for result in results:
            return_string += "<p>" + str(result[0]) + f" in row {result[1]} </p>"
        return return_string

    except ValueError:
        return abort(404)

@app.route('/all/<string:column_of_interest>')
def fetch_column(column_of_interest):
    try:
        return_string = """"""
        results = fetch_column_data(column_of_interest)
        for result in results:
            return_string += "<p> " + str(result[0]) + f" in row {result[1]} </p>"
        return return_string

    except ValueError:
        return abort(404)

@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    return "This is not a valid page! Please review README.md for valid paths and usage."

app.run(debug=True, port=8000)