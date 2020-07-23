from flask import Flask

app = Flask(__name__)

@app.route('/home/<int:id>')
def home(id):
    input = str(id)
    return '<h3>Id Anda : '+input+'</h3'

if __name__ == '__main__':
    app.run(debug=True)