from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Aku sayang Tata banget</h1>'

if __name__ == '__main__':
    app.run(debug=True)