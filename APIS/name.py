from flask import*
app=Flask(__name__)
@app.route('/login',methods=["POST","GET"])
def login():
    return render_template('name.html')
if __name__=='__main__':
    app.run(debug=True)