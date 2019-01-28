# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

Users = ['A', 'B', 'C']

@app.route('/hello/', methods = ['POST', 'GET'])
@app.route('/hello/<name>', methods = ['POST', 'GET'])
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/profile/', methods = ['POST', 'GET'])
def profile(username = None):
    error = None

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        print(username)
        print(email)
        return redirect(url_for('hello', name = username))

    if request.method == 'GET':
        username = request.args.get('username')
        email = request.args.get('email')
        print(username)
        print(email)

    error = 'Invalid username or email'
    return render_template('hello.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)