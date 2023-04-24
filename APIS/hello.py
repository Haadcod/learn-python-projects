from flask import Flask, url_for
from werkzeug.utils import redirect

app=Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name
if __name__=='__main__':
    app.run(debug=True)
#from flask import Flask
@app.route('/blog/<int:Postig>')
def show_blog(Postid):
    return 'Blog number %d'% Postid
@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f'%revNo
#if __name__=='__main':
 #  app.run(debug=True)
#url routing in flask
@app.route('/admin')
def hello():
    return 'Hello admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest
@app.route('/user/<user>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('hello_guest',guest=name))
if __name__=='__main__':
    app.run(debug=True)
