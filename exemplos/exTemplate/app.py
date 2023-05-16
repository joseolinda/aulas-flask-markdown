from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

carrinho = []

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/sobre")
def sobre():
    return render_template("paginas/sobre.html", \
        titulo_pagina="Sobre mim")
    
@app.route("/produto/adicionar/<id_prod>")
def adicionar_produto(id_prod):
    carrinho.append(id_prod)
    return render_template("paginas/carrinho.html", produtos=carrinho)
    
if __name__ == "__main__":
    app.run(debug=True)