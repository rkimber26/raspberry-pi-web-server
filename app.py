from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bob')
def bob():
    return 'bob is the best!'

@app.route('/robert')
def robert():
    return 'robert is the best!'

@app.route('/index.html')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    
