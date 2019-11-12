from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	if 'states' in request.args:
		return render_template('home.html', states = get_state_options(counties), highestTravelTime = fun_fact(request.args['states'], counties))
	else:
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

def fun_fact(state, counties):
		#county with the longest average travel time
	highestTravelTime = ["county", 0.0]
	for data in counties:
		if data['State'] == state:
			if highestTravelTime[1] < data['Miscellaneous']['Mean Travel Time to Work']:
				highestTravelTime[1] = data['Miscellaneous']['Mean Travel Time to Work']
				highestTravelTime[0] = data['County']
	return highestTravelTime
if __name__=="__main__":
    app.run(debug=False)
