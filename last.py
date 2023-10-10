from flask import Flask, redirect, flash
from uagents import Agent
import threading 
import asyncio

app = Flask(__name__)

agent_thread_status = None

def run_agent_2():
    global agent_thread_status
    agent_thread_status = "running"
    agent.run()
    agent_thread_status = "finished"
    return

async def print_hello():
    await asyncio.sleep(2)
    print("hello")

    return "printed enough hellos"

# event = threading.Event()
agent = Agent(name="alice",seed='42',port=8000)
task = asyncio.Task(print_hello())
agent._background_tasks.add(task)
agent_thread = threading.Thread(target=run_agent_2)

@app.route("/")
def index():
    return "home page"

@app.route("/agent")
def run_agent():
    global agent_thread_status
    agent_thread.start()

    if agent_thread_status == "finished":
        flash("The agent has finished running.")
        return redirect("/")

    return "you will now see an agent screen"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
