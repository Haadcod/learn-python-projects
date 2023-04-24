from flask import*
app=Flask(__name__)
@app.route('/')
def map():
    return 'This is aa page for students marks'
@app.route('/success/<int:score>')
def success(score):
    return 'nsubuga abdulhaad passed with marks'+ str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return 'nsubuga abdulhaad failed with marks:'+str(score)
if __name__=='__main__':
    app.run()