from flask import*
app=(__name__)
app.secret_key='abc'
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login1.html')
@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        session['uname']=request.form['uname']
        return render_template('success.html')
@app.route('/logout')
def logout():
    if 'uname' in session:
        session.pop('uname',None)
        return render_template('logout.html')
    else:
        return 'user already logged out'
@app.route('/prfile')
def profile():
    if 'uname' in session:
        uname=session['uname']
        return render_template('profile.html',name=uname)
    else:
        return 'Please login first'
if __name__=='__main__':
    app.run()