from flask import Flask, render_template, request, make_response, url_for
from werkzeug.utils import redirect

app=Flask(__name__)
@app.route('/error')
def error():
    return '<p><strong>Enter correct password</strong></p>'
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/success',methods=["POST","GET"])
def success():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']
    if password=="haad":
        res=make_response(render_template('success.html'))
        res.set_cookie('email',email)
        return res
    else:
        return redirect(url_for("error"))
@app.route('/viewprofile')
def profile():
    email=request.cookies.get('email')
    res=make_response(render_template('profile.html',name=email))
    return res
if __name__=='__main__':
    app.run()