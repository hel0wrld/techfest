import asyncio
import os
from uagents import Agent, Context 
from flask import Flask, request
from flask import render_template
from .api.weatherAPI import WeatherAPI
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='templates', static_folder='static')
socket = SocketIO(app)

alice = Agent(name='techfest', seed='any random secret')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/techfest/", methods=['POST'])
def techfest():
    if request.method == 'POST':
        location = request.form['location']
        # Do something with the 'location' value, e.g., print it
        print(f"Received location: {location}")
        weather = WeatherAPI(location, 10, 20);
        weather.get_temperature()
        response = weather.return_json 
        print(response)       
        return render_template('index.html', response=response)
    
@app.route("/location", methods=['POST'])
def weather_response():
    if request.method == 'POST':
        location = request.form['location']
        # Do something with the 'location' value, e.g., print it
        print(f"Received location: {location}")
        weather = WeatherAPI(location, 10, 20)
        weather.get_temperature()
        response = weather.return_json 
        return response 

@alice.on_interval(period=2.0)
async def get_weather_data():
    weather = WeatherAPI('london', 10, 20)
    await weather.get_temperature()
    response = weather.return_json
    socket.emit(response)

@socket.on('connect')
def handle_connect():
    print('Connected!!')
    socket.start_background_task(target= get_weather_data)

# @alice.on_interval(period=10.0)
# async def on_interval(info_object):
#     # Your asynchronous code here
#     weather = WeatherAPI(
#         info_object['location'], 
#         info_object['lower_temp'],
#         info_object['upper_temp']
#     )
#     weather.get_temperature()
#     in_range = asyncio.create_task(weather.check_temperature())
#     await in_range
#     print(f"Is temperature in range? {in_range}")
#     print(weather)
#     return weather

@app.route("/techfest/location/check_temperature", methods=['POST'])
async def uagent():
    lower_temp = request.form['lowerTemp']
    upper_temp = request.form['upperTemp']

    location = "London"
    lower_temp = 10
    upper_temp = 20
    info_object = {
        "location": location,
        "lower_temp": lower_temp,
        "upper_temp": upper_temp,
    }
    

if __name__ == '__main__':
    # Start the Alice agent.
    alice.start()

    # Start the Flask app.
    app.run()