from flask import render_template
from app import app
from models.order_list import order

@app.route('/')
def index():
    return render_template('index.html', title='Home', order_var=order)

@app.route('/order/<int:id>')
def single_order(id):
    return render_template("order.html", title="Single Order", order=order[id])


