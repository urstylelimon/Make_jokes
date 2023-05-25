import requests

def random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    joke_setup = joke_data["setup"]
    joke_punchline = joke_data["punchline"]
    return joke_setup, joke_punchline

setup, punchline = random_joke()
print("Question: " + setup)
print("Answer: " + punchline)

