from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')


@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/quienes')
def quienes():
    return render_template('quienes.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
=======

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

>>>>>>> 1545e04ca7aa2b3e39dcde839131cf3a7d24e847

if __name__ == '__main__':
    app.run(debug=True)
