from flask import Flask
app=Flask(__name__)
@app.route('/login')
def login():
    return 'This is nsubuga abdulhaad page for student results'
@app.route('/success/<int:score>')
def success(score):
    return 'The student passed with:'+str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return 'The student failed with :'+str(score)
@app.route('/result/<int:score>')
def result(score):
    result=""
    if score<50:
        result='fail'
    else:
        result='pass'
    return result
if __name__=='__main__':
    app.run()