from flask import*
app=Flask(__name__)
@app.route('/')
def customer():
    return render_template('customer.html')
@app.route('/sucess',methods=['POST','GET'])
def print_data():
    if request.method=='POST':
        result=request.form

if __name__=='__main__':
    app.run(debug=True)
