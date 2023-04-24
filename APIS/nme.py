from flask import Flask
app=Flask(__name__)
@app.route('/')
def login():
    return 'This is my name'
if __name__=='__main__':
    app.run()