from flask import Flask, render_template
app = Flask(__name__, template_folder = "templates", static_folder = "static")

test_name = 'Python test'
max_score = 100

students = [
    {'name': 'Misha', 'score': 97},
    {'name': 'Kate', 'score': 95},
    {'name': 'Glib', 'score': 90},
    {'name': 'Sergiy', 'score': 100},
    {'name': 'Kostya', 'score': 57}
]

@app.route('/')
def index():
    context = {
        'title': "Results",
        'students': students,
        'test_name': test_name,
        "max_score": max_score
    }
    return render_template('results.html', **context)

if __name__ == '__main__':
  app.run(port= 7050, debug=True)