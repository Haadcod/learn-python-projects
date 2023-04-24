from flask import*
app=Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    uname=str(request.form['uname'])
    paswrd=request.form['pass']
    if uname=='nsubuga'and paswrd=='haad':
        return 'Welcome %d'%uname
if __name__=='__main__':
    app.run(debug=True)
