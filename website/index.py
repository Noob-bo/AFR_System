from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/eso')
def ESO():
    return render_template('Manteniment.html')

@app.route('/batx')
def batx():
    return render_template('batx.html')

@app.route('/entrenament')
def entrenament():
    import Entrenador
    return render_template('EntrenamentOK.html')

@app.route('/afegir_alumne')
def afegir():
    import persones_a_afegir
    return render_template('AlumnesOK.html')

@app.route('/passar_llista')
def llista():
    exec(open('passar_llista.py').read())
    return render_template('LlistaOK.html')

if __name__ == '__main__':
    app.run(debug = True)

