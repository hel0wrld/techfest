import sys
from uagents import Agent, Context 
from api.weatherAPI import WeatherAPI

alice = Agent(name='techfest', seed='any random secret')

@alice.on_interval(period=10.0)
async def on_interval(ctx: Context):
    
    location = sys.argv[1]
    lower_temp = float(sys.argv[2])
    upper_temp = float(sys.argv[3])
    # print(location, lower_temp, upper_temp)
    
    weather = WeatherAPI(location, lower_temp, upper_temp)
    weather.get_temperature()
    in_range = weather.check_temperature()
    
    ctx.logger.info(f'For {location}, {lower_temp}, {upper_temp}, temperature is {weather.return_json["current"]["temp_c"]}, so in range: {in_range}')
    
if __name__ == '__main__':
    alice.run()
