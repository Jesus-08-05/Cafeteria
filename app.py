from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes')
def quienes():
    return render_template('quienes.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)
