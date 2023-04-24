from flask import*
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
def login():
    error=None;
    if request.method=='POST':
        if request.form['pass']=='haad':
            error='invalid password'
if __name__=='__main__':
    app.run()