from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


if __name__ == '__main__':
    app.run(debug=True)
