from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'any random string'


# @app.route('/')
# def student():
#     return render_template('student.html')
# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/setcookie', methods=['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['nm']
#
#     resp = make_response(render_template('readcookie.html'))
#     resp.set_cookie('userID', user)
#
#     return resp

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template("login.html",result = result)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run()
