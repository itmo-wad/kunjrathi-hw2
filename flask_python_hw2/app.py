from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flask-hw2'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask-hw2'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            if 'password' in request.form and request.form['password'].encode('utf-8') == login_user['password'].encode('utf-8'):
                return redirect(url_for('profile'))
        return "Invalid username or password"
    else:
        return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = "secretkeyhere"
    app.run(host="localhost", port=5000, debug=True)