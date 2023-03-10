from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"

# Connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['USERS']


# Home page
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/Logineg')


# Signup page
@app.route('/SignUpeg', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists in database
        if db.users.find_one({'username': username}) is not None:
            return render_template('SignUpeg.html', error='Username already exists')

        # Insert new user into database
        db.users.insert_one({'username': username, 'password': password})

        # Store username in session and redirect to home page
        session['username'] = username
        return redirect('/')

    else:
        return render_template('SignUpeg.html')


# Login page
@app.route('/Logineg', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password are correct
        user = db.users.find_one({'username': username, 'password': password})
        if user is not None:
            # Store username in session and redirect to home page
            session['username'] = username
            return redirect('/')
        else:
            return render_template('Logineg.html', error='Invalid username or password')

    else:
        return render_template('Logineg.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/Logineg')


if __name__ == '__main__':
    app.run(debug=True)
