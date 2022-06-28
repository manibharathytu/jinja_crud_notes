
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from pickle_db import save_to_pickle_db, read_from_pkl_db
import notes_mgr


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.




@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('a.html', data={'a': {'data': ['a']}, 'b': {'data': ['b']}})
    return 'Hello World'


@app.route('/notes')
def get_notes():
    notes_data = notes_mgr.get_notes_data()
    return render_template('notes_page.html', notes_data=notes_data)


# @app.route('/addNote', methods=['POST', 'GET'])
# def add_notes():
#     print(request.get_data())
#     return render_template('notes_page.html', notes_data=notes_data)


@app.route('/crud', methods=['POST', 'GET'])
def crud_notes():
    notes_mgr.notes_crud(request.get_json())

    # return render_template('notes_page.html', notes_data=notes_data)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
