from flask import Flask

app = Flask(__name__)

@app.route('/home/<string:name>')
def home(name):
    return 'Name : '+name

if __name__ == '__main__':
    app.run(debug=True)