from flask import Flask

app = Flask(__name__)

@app.route('/')
def greetings():
    return 'Hello user'

@app.route('/menu')
def menu():
    return "This is menu page"

if __name__ == "__main__":
    app.run(port=7000)