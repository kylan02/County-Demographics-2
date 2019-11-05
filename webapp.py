from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	return render_template('home.html', states = get_state_options(counties))

def get_state_options(counties):
	listOfStates = []
	for data in counties:
		if data['State'] not in listOfStates:
			listOfStates.append(data['State'])
	options = ""
	for data in listOfStates:
		options = options + Markup("<option value=\""+data+"\">"+data+"</option>")
	return options

if __name__=="__main__":
    app.run(debug=False)
