from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder="static")


A = 'Name'
B = 'Ingridients'
C = 'Price'

a = 'Mozzarela'
b = f'cheese, basil, tomatoes'
c = 120

d = 'Carbonara'
e = f'basil, eggs, Parmesan, Mozzarela'
f = 130

g = 'Pepperoni'
h = f'salami, cream sauce, basil, tomatoes'
i = 85

j = 'Four cheese'
k = f'Parmesan, Adyghe, Mozzarella, Dorblu'
l = 90

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    context = {
        'title': "Menu restaurant",
        'A': A,
        'B': B,
        'C': C,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
    }
    return render_template('menu.html', **context)

if __name__ == '__main__':
    app.run(port= 7000, debug=True)