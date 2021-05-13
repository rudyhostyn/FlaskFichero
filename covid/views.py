from covid import app

@app.route("/")
def index():
    return "Flask funciona"