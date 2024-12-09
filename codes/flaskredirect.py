from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Homepage!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username == "admin":
            return redirect(url_for('dashboard'))
        else:
            return "Invalid login. Try again."
    return '''
        <form method="post" action="/login">
            <input type="text" name="username" placeholder="Enter username">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
