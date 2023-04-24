from flask import Flask, make_response, session, render_template

app=Flask(__name__)
app.secret_key='abc'
@app.route('/')
def home():
    res=make_response('<h4>The session is set, <a href="/get">Get variable</a></h4>')
    session['response']='nsubuga session'
    return res
@app.route('/get')
def getvariable():
    if 'response' in session:
        s=session['response'];
        return render_template('getsession.html',name=s)
if __name__=='__main__':
    app.run()
