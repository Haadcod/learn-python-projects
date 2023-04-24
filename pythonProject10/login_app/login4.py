from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home2.html')
@app.route('/login')
def login():
    return render_template('login4.html')
@app.route('/validate',methods=['POST'])
def validate():
    if request.method=='POST' and request.form['pass']=='haad':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('login'))
@app.route('/success')
def success():
    return 'logged in successfully'
if __name__=='__main__':
    app.run()