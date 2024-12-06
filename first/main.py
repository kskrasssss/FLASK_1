from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

@app.route('/')
def index():
    return render_template('index.html', title = 'Hello and welcom to Jinjia2')





test_name = 'Python test'
max_score = 100

students = [
    {'name': 'Misha', 'score': 97},
    {'name': 'Kate', 'score': 95},
    {'name': 'Glib', 'score': 90},
    {'name': 'Sergiy', 'score': 100},
    {'name': 'Kostya', 'score': 57}
]

@app.route('/results')
def results():
    context = {
        'title': "Results",
        'students': students,
        'test_name': test_name,
        "max_score": max_score
    }
    return render_template('results.html', **context)





projects = [
    {'name': 'Game-1', 'year': 2021},
    {'name': 'Game-2', 'year': 2023},
    {'name': 'Game-3', 'year': 2019},
]

@app.route('/portfolio')
def portfolio():
    context = {
        'title': 'Portfolio',
        'projects': projects
    }
    return render_template('portfolio.html', **context)

if __name__ == "__main__":
    app.run(port=7000, debug=True)