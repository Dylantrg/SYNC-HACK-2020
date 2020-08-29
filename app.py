from flask import Flask, render_template, request, jsonify, flash, url_for, redirect, session
from database import project_schema, user_schema, projects
import time

# import utils

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in user or request.form['password'] not in user['username']:
            error = 'The username or the password is incorrect. Please try again. '
        else:
            #Straight to the dashboard.html page. 
            return redirect(url_for('dashboard'))   
       
    return render_template('app.js', error=error)

@app.route('/Log out')
def logout():
    flash("You were logged out")
    return redirect(url_for('app.js'))

@app.route("/process", methods=['POST'])
def match_preference():
    # user_tags = request.form['tags']   # list of strings
    # user_reqs = request.form['resources'] # list of strings
    # # more user_relevant features

    return jsonify(sorted_projects)
    # return "ANOTHER HELLO WORLD!"
    # pass_required = utils.filter(projects, user_reqs)
    # sorted_projects = sorted(projects, key=utils.string_match())

# Called whenever a checkbox is ticked/unticked
# Updates projects shown on page based on preferences chosen
current_preferences = []
@app.route('/update_preferences', methods=['POST'])
def update_preferences():
    print("Hello")
    jsondata = request.get_json()
    print(jsondata)
    pref_name = jsondata['pref_name']   # name of preference ticked/unticked
    pref_ticked = jsondata['pref_value'] # preference ticked or not
    print(pref_name, pref_ticked) # testing
    current_preferences.append(pref_name)
    # RUN SORT
    if pref_ticked and len(current_preferences) == 1: # Just add projects
        # Search projects list for one with corresponding preference t
        for project in projects:
            if project[]

    # RETURN ranked projects
    return "Placeholder"

if __name__ == "__main___":
    app.run(debug=True)
