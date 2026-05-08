from flask import Flask, request, redirect, url_for, abort
import dotenv
import ProductionCode.datasource as database
from ProductionCode.command_line import *

app = Flask(__name__)
app.config['DEBUG'] = True
conn = database.connect()

@app.route('/')
def home():
    return "Please look at the README.md to learn what routes to go to!"

# TO-DO: UPDATE PATHS TO USE THE SQL METHODS/FUNCS; THIS REQUIRES DEBUGGING ABILITY
@app.route('/<string:column_of_interest>')
def top_5_columns(column_of_interest):
    try:
        return_string = """"""
        # results = nafees_user_story(column_of_interest)
        results = database.get_top_n_column_values_SQL(conn, column_of_interest, 5)
        return_string += f"<h1> Top 5 Models by {column_of_interest} </h1>"
        for result in results:
            return_string += "<p> Model:" + str(result[0]) + f" | {result[1]} </p>"
        return return_string
    
    except ValueError:
        return abort(404)

@app.route('/<int:n>/<string:column_of_interest>')
def top_n_columns(column_of_interest, n):
    try:
        return_string = """"""
        # results = top_n_column_values(column_of_interest, n)
        results = database.get_top_n_column_values_SQL(conn, column_of_interest, n)
        return_string += f"<h1> Top 5 Models by {column_of_interest} </h1>"
        for result in results:
            return_string += "<p> Model:" + str(result[0]) + f" | {result[1]} </p>"
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