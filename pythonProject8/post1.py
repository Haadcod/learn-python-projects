from flask import*
app=Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passw=request.form['pass']
    if uname=='nsubuga' and passw=='haad':
        return 'welcome to my page %s'%uname

if __name__=='__main__':
    app.run()