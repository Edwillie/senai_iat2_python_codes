from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/contatos")
def contato():
    return render_template("contatos.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operacao = request.form.get("operacao")

        if operacao == "add":
            resultado = num1 + num2
        elif operacao == "sub":
            resultado = num1 - num2
        elif operacao == "div":
            resultado = num1 / num2 if num2 != 0 else "Erro ao dividir por zero!"                      
        elif operacao == "mul":
            resultado = num1 * num2             
        else:
            resultado = 0

    return render_template("calculadora.html", resultado = resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0')