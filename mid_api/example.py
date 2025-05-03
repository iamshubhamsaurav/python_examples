from main import MidAPI

app = MidAPI()

@app.get('/app')
def home_app():
    return "Hello"