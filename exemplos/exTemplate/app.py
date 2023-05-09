from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/sobre")
def sobre():
    return render_template("paginas/sobre.html", \
        titulo_pagina="Sobre mim")
    
@app.route("/teste")
def teste():
    return "está atualizando de verdade"
    
if __name__ == "__main__":
    app.run(debug=True)