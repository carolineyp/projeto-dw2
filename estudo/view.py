from estudo import app
from flask import render_template , request, redirect, url_for

@app.route ('/')
def formulario():
    return render_template ('index.html')

@app.route ('/resultado', methods = ['POST'])
def resultado():
     nome = request.form['nome']
     peso = float(request.form['peso'])
     altura = float(request.form['altura'])
     imc = round(peso / (altura ** 2), 2)

     if imc < 18.5:
        situacao = "Abaixo do peso"
     elif imc < 25:
        situacao = "Peso normal"
     elif imc < 30:
        situacao = "Sobrepeso"
     else:
        situacao = "Obesidade"

     return render_template('resultado.html', nome=nome, imc=imc, situacao=situacao)


@app.route('/autor')
def autor():
    return render_template('autor.html')

if __name__ == '__main__':
    app.run(debug=True)




