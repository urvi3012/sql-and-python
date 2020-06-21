from flask import Flask,request,render_template

    
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return 'hello %s'%name

if __name__ == '__main__':
    app.run(debug=True)
