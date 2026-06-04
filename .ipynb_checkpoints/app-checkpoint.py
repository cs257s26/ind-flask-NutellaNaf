from flask import Flask, request, redirect, url_for, abort
import dotenv
import ProductionCode.datasource as database
# from ProductionCode.command_line import *
import sys

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
        # print(results)
        return_string += f"<h1> Top 5 Models by {column_of_interest} </h1>"
        for result in results:
            return_string += "<p> Model:" + str(result[0]) + f" | {result[1]} </p>"
        print(f"\n \n \n{return_string}\n\n\n")
        return return_string
    
    except Exception:
        return abort(404)

@app.route('/<int:n>/<string:column_of_interest>')
def top_n_columns(column_of_interest, n):
    try:
        return_string = """"""
        # results = top_n_column_values(column_of_interest, n)
        results = database.get_top_n_column_values_SQL(conn, column_of_interest, n)
        return_string += f"<h1> Top {n} Models by {column_of_interest} </h1>"
        for result in results:
            return_string += "<p> Model:" + str(result[0]) + f" | {result[1]} </p>"
        print(f"\n \n \n{return_string}\n\n\n")
        return return_string

    except Exception:
        return abort(404)

@app.route('/all/<string:column_of_interest>')
def fetch_column(column_of_interest):
    try:
        return_string = """"""
        # results = fetch_column_data(column_of_interest)
        results = database.get_whole_column_SQL(conn, column_of_interest)
        print(f"these are results: {results} \n \n")
        model_attribution = database.get_whole_column_SQL(conn, "model_name")
        return_string += f"<h1> All values in {column_of_interest} </h1>"
        return_string += "<ol>"
        for i in range(len(results)):
            return_string += f"<li> Model: {model_attribution[i][0]} | Value: {results[i][0]} </li>"
        return_string += "</ol>"
        print(f"\n \n \n{return_string}\n\n\n")
        return return_string

    except Exception:
        return abort(404)

@app.route('/model/<string:model_name>')
def row_by_model(model_name):
    try:
        return_string = """"""
        # results = fetch_column_data(column_of_interest)
        results = database.get_row_by_model_name_SQL(conn, model_name)
        # print(model_name)
        model_tuple = (model_name, )
        print(model_tuple)
        print("\n")
        # all_models = database.get_whole_column_SQL(conn, "model_name")
        # print(f"all_models: {all_models}\n")
        # print(f"all_models_0: {all_models[0]}")
        return_string += f"<h1> Info for {model_name} </h1> <br>"
        return_string += """<table border=1> <thead> <tr> """
        for i in range(len(results[0])):
            return_string += f"<th>{results[0][i]}</th>"
        return_string +="""</tr> </thead> <tbody> <tr>"""
        
        for i in range(len(results[0])):
            return_string += f"""<td>{results[1][i]}</td>"""
        return_string += """</tr> </tbody> </table>"""

        print(f"\n \n \n{return_string}\n\n\n")
        return return_string

    except Exception:
        return abort(404)

@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    return "This is not a valid page! Please review README.md for valid paths and usage."

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5123
    app.run(host='stearns.mathcs.carleton.edu', port=port)