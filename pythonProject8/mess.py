from flask import Flask
app=Flask(__name__)
@app.route('/')
def message():
    return '<html><body><h1>This is my website</h1></body></html>'
if __name__=='__main__':
    app.run()