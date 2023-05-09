---
theme : "night"
transition: "concave"
highlightTheme: "github-dark-dimmed"
slideNumber: true
title: "Aula 01 - Introdução ao Flask"
customTheme: "assets/pweb1"

---
<!-- .slide: data-background="#4d7e65" -->
# Programação Web I - Flask
![Flask](/assets/logo-flask.png "Logo do Flask"){width=100px}
## Aula 02 - Rotas

Prof. José Olinda

---

## Conteúdos


* O que são rotas?
* Rotas dinâmicas
* TIpos de Parâmetros de rotas
* Criar uma aplicação com rotas em Flask dinâmicas

---

<!-- .slide: data-background="#4d7e65" -->
# O que são rotas?

* Rotas são os caminhos que o usuário pode acessar em uma Aplicação Web
* São definidas no servidor
* Cada rota é associada a uma função
* A função é executada quando o usuário acessa a rota

--

<!-- .slide: data-background="#4d7e65" -->
## Declaração de rotas

* Rotas são definidas com o decorador `@app.route()`
* O decorador recebe como parâmetro o caminho da rota
* O caminho da rota é uma string que começa com `/`
* Ao acessar a rota, a função associada é executada, geralmente retornando uma página HTML


--


## Exemplo de rotas

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'About page'
```

---

<!-- .slide: data-background="#4d7e65" -->
# Rotas dinâmicas

* Rotas dinâmicas são rotas que recebem parâmetros
* Os parâmetros são definidos entre `<` e `>`
* Os parâmetros são passados para a função associada à rota
* As rotas dinâmicas permitem criar páginas dinâmicas, ou seja, que mudam de acordo com o parâmetro passado

--

## Exemplo de rota dinâmica

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
```

--

## Como funciona?

* Quando o usuário acessa a rota `/user/joseolinda`, o Flask chama a função `show_user_profile` passando o parâmetro `username` com o valor `joseolinda`
* A função `show_user_profile` retorna a string `User joseolinda`
* Pode ser usado para criar páginas dinâmicas, como páginas de perfil de usuário, por exemplo
* Uma única rota pode retornar páginas diferentes de acordo com o parâmetro passado

| URL | Resultado |
|-----|-----------|
| `/user/joseolinda` | `User joseolinda` |
| `/user/fulano` | `User fulano` |
| `/user/ciclano` | `User ciclano` |

---

<!-- .slide: data-background="#4d7e65" -->

# Tipos de parâmetros de rotas

* Por padrão, os parâmetros de rotas são strings
* É possível definir o tipo do parâmetro

| Tipo | Descrição |
|------|-----------|
| `string` | (padrão) aceita qualquer texto sem barra |
| `int` | aceita números inteiros |
| `float` | aceita números de ponto flutuante |
| `path` | aceita qualquer texto, incluindo barras |

--

### Exemplos

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/float/<float:float_number>')
def show_float(float_number):
    return 'Float %f' % float_number
```

---

<!-- .slide: data-background="#4d7e65" -->
#### Exemplo de Rotas Rede Social de Foto
<pre><code data-line-numbers="1-9|10-14">from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Bem-vindo ao Flaskgram!'
@app.route('/perfil/&ltusername&gt')
def perfil(username):
    return 'Perfil do usuário %s' % username
@app.route('/feed/&gtint:post_id&gt')
def feed(post_id):
    return 'Foto %d' % post_id
@app.route('/feed/&ltint:post_id&gt/comentarios')
def comentarios(post_id):
    return 'Comentários da foto %d' % post_id
</code></pre>

---

# Dúvidas?

### jose.olinda@ifce.edu.br