
from flask import Flask,render_template,url_for

app= Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def hello():
    return 'Hey Niru'

if __name__ =='__main__':
    app.run(host = '0.0.0.0',port = 3000,debug = True)