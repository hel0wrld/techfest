from flask import Flask
from uagents import Agent, Context
import threading 

app = Flask(__name__)

# Create an agent
agent = Agent(name="alice",seed='42')

@app.route("/")
def index():
    return "home page"

@app.route("/agent")
def run_agent():
    # Start the agent
    agent.run()

    # Schedule the agent to run periodically
    agent.on_interval(period=2.0, callback=print_bs)

    # Return a message to the user
    return "Agent started!"

@agent.on_interval(period=2.0)
async def print_bs(ctx):
    print("hi hello")
    return "Agent started!"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)