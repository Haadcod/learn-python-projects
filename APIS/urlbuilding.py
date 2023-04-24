from flask import Flask, url_for
from werkzeug.utils import redirect

app=Flask(__name__)
@app.route('/admin')
def admin():
    return 'I am admin'
@app.route('/liberation')
def liberation():
    return 'I liberated this country'
@app.route('/student')
def student():
    return 'I am a student'
@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='liberation':
        return redirect(url_for('liberation'))
    if name=='student':
        return redirect(url_for('student'))
if __name__=='__main__':
    app.run(debug=True)
