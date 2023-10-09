import requests
from time import sleep

max_tries = 3
url = "https://weatherapi-com.p.rapidapi.com/current.json"

class WeatherAPI:
    
    """
        weather api doc
    """
    
    def __init__(self, location, temp_lower, temp_higher):
        self.location = location
        self.temp_lower = temp_lower
        self.temp_higher = temp_higher
        self.return_json = ''
    
    async def get_temperature(self):

        querystring = {"q":self.location}
        headers = {
            "X-RapidAPI-Key": "197ce8a65dmsh8cd843f8b6cb242p1b55dbjsn1813a0041bea",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        for _ in range(max_tries):
            try:
                response = await requests.get(url, headers=headers, params=querystring)
                self.return_json = response.json()
                break
            except requests.exceptions.RequestException:
                print("Error occurred!! Retrying...")
                sleep(0.5)
        else:
            print("Max tries completed! couldn't fetch data :(")
        
    def check_temperature(self):
        
        print(self.return_json)
        temp_c = self.return_json['current']['temp_c']
        if temp_c >= self.temp_lower and temp_c <= self.temp_higher:
            return True
        else:
            return False
        # return True
