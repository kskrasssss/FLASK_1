from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizza = [
        {'name': 'Mozzarela', 'ingridients': 'cheese, basil, tomatoes', 'price': 120},
        {'name': 'Carbonara', 'ingridients': 'basil, eggs, Parmesan, Mozzarela', 'price': 75},
        {'name': 'Pepperoni', 'ingridients': 'salami, cream sauce, basil, tomatoes', 'price': 90},
        {'name': 'Four cheese', 'ingridients': 'Parmesan, Adyghe, Mozzarella, Dorblu', 'price': 110},
    ]

    context = {
        'pizza': pizza,
    }
    return render_template('menu.html', **context)

if __name__ == '__main__':
    app.run(port= 7000, debug=True)
