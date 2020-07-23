from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h3>Hello</h3>'

if __name__ == '__main__':
    app.run(debug=True)