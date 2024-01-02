from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# データベースファイルのパスを設定
DATABASE = 'path/to/your/database.db'

# データベース接続用のヘルパー関数
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
