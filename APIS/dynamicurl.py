from flask import Flask
app=Flask(__name__)
@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}!'
@app.route('/hello')
def hello():
    return 'welcome to geekforgeeks'
@app.route('/')
def index():
    return 'I am a student'
if __name__=='__main__':
    app.run(debug=True)