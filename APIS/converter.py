from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/hello/<int:id>')
def show_post(id):
    return f'this is geekforgeeks page {id}'
@app.route('/hello2/<username>')
def show_user(username):
    return f'this is the username {username}'
@app.route('/haad')
def welcome():
    return 'hello, welcome to geekforgeeks'
@app.route('/product/<name>')
def get_product(name):
    return f'The product is {name}'
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest' %guest
@app.route('/user/<username>')
def hello_username(username):
    if username=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=username))
if __name__=='__main__':
    app.run(debug=True)