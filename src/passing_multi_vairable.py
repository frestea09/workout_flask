from flask import Flask

app = Flask(__name__)

@app.route('/home/<int:id>/<string:name>')
def home(id,name):
    inputId = str(id)
    inputName = str(name)
    return '<h3>Selamat Datang %s , id anda %s</h3>'%(inputId,inputName)

if __name__ == '__main__':
    app.run(debug=True)