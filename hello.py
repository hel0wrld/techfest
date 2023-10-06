import asyncio
from uagents import Agent, Context 
from flask import Flask, request
from flask import render_template
from .api.weatherAPI import WeatherAPI

app = Flask(__name__, template_folder='templates', static_folder='static')

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

@app.route("/techfest/location/check_temperature", methods=['POST'])
async def uagent():
    response = {}
    lower_temp = request.form['lowerTemp']
    upper_temp = request.form['upperTemp']
    
    # Create an instance of Agent
    alice = Agent(name='techfest', seed='any random secret')
    
    location = "London"
    lower_temp = 10
    upper_temp = 20
    @alice.on_interval(period=10.0)
    async def on_interval(ctx: Context):
        # Your asynchronous code here
        weather = await WeatherAPI(location, lower_temp, upper_temp)
        weather.get_temperature()
        in_range = weather.check_temperature()
        response = weather.return_json 
        ctx.logger.info(f'For {location}, {lower_temp}, {upper_temp}, temperature is {weather.return_json["current"]["temp_c"]}, so in range: {in_range}')
        return render_template('agent.html', response=response) 
    
    # alice.on_interval(period=10.0)     
        
    alice.run(debug=True)
    return None
