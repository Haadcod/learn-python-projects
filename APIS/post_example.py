from flask import*
app=Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=='nsubuga' and password=='google':
        return 'welcome %s'%uname
    if __name__=='__main':
        app.run(debug=True)