from flask import*
app=Flask(__name__)
@app.route('/login',methods=["GET"])
def login():
    uname=request.args.get('uname')
    passw=request.args.get('pass')
    if uname=='nsubuga' and passw=='haad':
        return 'Welcome to my new page %s'%uname
    else:
        return 'Invalid username'

if __name__=='__main__':
    app.run()