from flask import*
app=Flask(__name__)
@app.route('/login',method=['POST'])
def login():
    uname=request.form['uname']
    password=request.form['password']
    if uname=='nsubuga' and password=='haad':
        return 'Welcome to page %s'%uname
    else:
        return 'Invalid login'
if __name__=='__main__':
    app.run(debug=True)