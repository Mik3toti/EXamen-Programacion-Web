from flask import Flask, request
from flask import render_template


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("index.html")

@app.route('/ejercicio1',methods=["GET","POST"])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        pintura = int(request.form['pintura'])
        tarros = 9000
        #calculo =
        total = pintura * tarros
        #pago =  round(total - (total * calculo))

        if 18 <= edad <= 30:
            calculo =  0.15
        elif edad > 30:
            calculo =  0.25
        else:
            calculo = 0


        descuento = total * calculo
        pago = total - (total * calculo)

        return render_template('ejercicio1.html',nombre=nombre , edad=edad, pintura=pintura, calculo=calculo, tarros=tarros, total=total, pago=pago, descuento=descuento)
    return render_template("ejercicio1.html")


@app.route('/ejercicio2',methods=["GET","POST"])
def ejercicio2():
    bienvenida = None
    incorrecto = None
    if request.method == 'POST':
        user = str(request.form['user'])
        password = str(request.form['password'])
        #incorrecto= "Usuario o contraseña incorrectos"


        if user == "juan" and password =="admin":
            bienvenida = "Bienvenido Administrador"
        elif user == "pepe" and password == "user":
            bienvenida= "Bienvenido Usuario"
        else:
            incorrecto = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html',user=user, password=password, incorrecto=incorrecto, bienvenida=bienvenida)

    return render_template("ejercicio2.html")



if __name__ == '__main__':
    app.run(debug=True)