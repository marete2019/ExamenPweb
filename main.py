from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        total = tarros * 9000

        if 18 <= edad <= 30:
            descuento = 15
        elif edad > 30:
            descuento = 25
        else:
            descuento = 0

        total_pagar = total - (total * descuento / 100)

        return render_template("ejercicio1.html", nombre=nombre, total=total, descuento=descuento,
                           total_pagar=total_pagar)
    return render_template(ejercicio1.html)


@app.route('/Ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."



    return render_template('Ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
