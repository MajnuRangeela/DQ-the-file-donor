from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'For Ping Purpose Only!'

if __name__ == "__main__":
    app.run()