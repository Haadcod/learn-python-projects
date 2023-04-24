from flask import Flask
app=Flask(__name__)
@app.route('/hello')
def function():
    return 'Hello nsubuga abdulhaad'
@app.route('/')
def index():
    return 'Welcome to geekforgeeks'
if __name__=='__main__':
    app.run(debug=True)