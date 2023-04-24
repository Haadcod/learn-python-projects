from flask import Flask, render_template

app=Flask(__name__)
@app.route('/user/<uname>')
def message():
    return render_template('message.html',name='uname')
if __name__=='__main':
    app.run(debug=True)