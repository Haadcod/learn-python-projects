from flask import*
app=Flask(__name__)
@app.route('/login',method=['GET'])
def login():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='nsubuga' and password=='haad':
        return 'Welcome %s'%uname
if __name__=='__main__':
    app.run(debug=True)