from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
from db_functions import add_todo_item, mark_complete, get_complete, get_incomplete,del_todo_item

app = Flask(__name__)


@app.route('/')
def index():
    incompleted = get_incomplete()
    completed = get_complete()
    return render_template('layout.html', incomplete=incompleted, complete=completed)


@app.route('/add', methods=['POST'])
def add():
    add_todo_item(text=request.form['ip'])
    return redirect(url_for('index'))

@app.route('/dele/<id>')
def dele(id):
    del_todo_item(id)
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    mark_complete(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)