from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home',methods = ['POST','GET'])
def index():
    if request.method=='GET':
        return '<h1>hey</h1>'
    else:
        return '<h2>hello</h2>'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)