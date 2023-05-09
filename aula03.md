---
theme : "night"
transition: "concave"
highlightTheme: "github-dark-dimmed"
slideNumber: true
title: "Aula 03 - Templates com Jinja2"
customTheme: "assets/pweb1"

---
<!-- .slide: data-background="#4d7e65" -->
# Programação Web I - Flask
![Flask](/assets/logo-flask.png "Logo do Flask"){width=100px}
## Aula 03 - Templates com Jinja2

Prof. José Olinda

---

## Conteúdos
<br />

::: { .container}
:::: {.col }
* O que são templates?
* Introdução ao Jinja2
* Configuração de templates em Flask
* Criando templates com Jinja2
* Herança de templates
* Inclusão de templates
::::
:::: {.col }
* Estruturas condicionais em Jinja2
* Estruturas de repetição em Jinja2
* Filtragem de dados em Jinja2
* Modelo de template base para aplicações web
* Criar uma aplicação com templates em Flask
::::

---

### O que são templates?

* **Definição de templates:** Um template é um arquivo que contém elementos estáticos e dinâmicos que são usados para criar um documento HTML
* **Finalidade:** apresentar dados dinâmicos em páginas HTML
* **Vantagem 1:** criar layouts HTML que podem ser reutilizados em várias páginas
* **Vantagem 2:** separar o código HTML do código Python, facilitando a manutenção
* **Vantagem 3:** páginas HTML com mais qualidade visual, podendo usar CSS e JavaScript

---

### Introdução ao Jinja2

* **Jinja2:** é um mecanismo de template para Python, padrão do Flask
* **Características:** 
    * sintaxe simples
    * fácil de aprender
    * flexível
    * seguro
    * rápido
    * amplamente utilizado

--

### Instalação do Jinja2

* **Instalação:** o Jinja2 já vem instalado com o Flask
* **Importação:** o Jinja2 é importado automaticamente pelo Flask
* **Documentação:** https://jinja.palletsprojects.com/

* Caso queira instalar o Jinja2 separadamente, use o comando
```bash
pip install jinja2`
```

---

### Configuração de templates em Flask

* **Configuração:** para usar templates em Flask, é necessário configurar o diretório onde os templates serão armazenados
* **Pasta `templates`:** o Flask procura por templates na pasta `templates` dentro do diretório do projeto
* **Passo 1:** criar a pasta `templates` dentro do diretório do projeto
* **Passo 2:** configurar o diretório `templates` no Flask
```python
from flask import Flask
app = Flask(__name__, template_folder='templates')
```

---

### Criando templates com Jinja2

* **Passo 1:** criar um arquivo HTML dentro da pasta `templates`
* **Passo 2:** criar um arquivo Python com o código da aplicação
* **Passo 3:** criar uma rota que renderiza o template

--

### Exemplo de template
* **Passo 1:** criar um arquivo HTML dentro da pasta `templates`
* Criar o arquivo `index.html` dentro da pasta `templates`

```html	
<!DOCTYPE html>
<html>
<head>
    <title>{{ titulo_pagina }}</title>
</head>
<body>
    <h1>{{ titulo_pagina }}</h1>
    <p>{{ conteudo }}</p>
</body>
</html>
```

--

### Exemplo de template
* **Passo 2:** criar um arquivo Python com o código da aplicação
* Criar o arquivo `app.py` dentro do diretório do projeto

```python
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', \
        titulo_pagina='Página inicial', \
        conteudo='Bem-vindo ao site de PWeb I')
```

---

### Herança de templates

* **Definição:** a herança de templates permite criar um template base que pode ser usado por outros templates
* **Vantagem:** permite criar um layout padrão para todas as páginas do site
* **Sintaxe:** 
```html
{% extends "nome_do_template.html" %}
```

--

### Exemplo de herança de templates
* **Passo 1:** criar um arquivo HTML dentro da pasta `templates`
* Criar o arquivo `base.html` dentro da pasta `templates`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block titulo_pagina %}{% endblock %}</title>
</head>
<body>
    <h1>{% block titulo_pagina %}{% endblock %}</h1>
    <p>{% block conteudo %}{% endblock %}</p>
</body>
</html>
```

--

### Exemplo de herança de templates
* **Passo 2:** criar um arquivo HTML dentro da pasta `templates`
* Criar o arquivo `index.html` dentro da pasta `templates`

```html
{% extends "base.html" %}
{% block titulo_pagina %}Página inicial{% endblock %}
{% block conteudo %}Bem-vindo ao site de PWeb I{% endblock %}
```

--

### Exemplo de herança de templates
* **Passo 3:** criar um arquivo Python com o código da aplicação
* Criar o arquivo `app.py` dentro do diretório do projeto

```python
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')
```

---

### Inclusão de templates

* **Definição:** a inclusão de templates permite criar um template que pode ser incluído em outros templates
* **Vantagem:** permite criar um componente HTML que pode ser reutilizado em várias páginas
* **Sintaxe:** 
```html
{% include "nome_do_template.html" %}
```

--

### Exemplo de inclusão de templates
* Considerando o template `base.html` criado anteriormente, vamos criar um template para o menu de navegação
* **Passo 1:** criar um arquivo HTML dentro da pasta `templates`
* Criar o arquivo `menu.html` dentro da pasta `templates`

```html
<nav>
    <a href="/">Home</a>
    <a href="/sobre">Sobre</a>
    <a href="/contato">Contato</a>
</nav>
```

--

### Exemplo de inclusão de templates
* **Passo 2:** incluir o template `menu.html` no template `base.html`
* Modificar o arquivo `base.html` dentro da pasta `templates`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block titulo_pagina %}{% endblock %}</title>
</head>
<body>
    {% include "menu.html" %}
    <h1>{% block titulo_pagina %}{% endblock %}</h1>
    <p>{% block conteudo %}{% endblock %}</p>
</body>
</html>
```

---

### Variáveis em templates

* O uso de variáveis em templates permite criar páginas dinâmicas, sem a necessidade de escrever o código HTML diretamente no Python
* **Sintaxe:** 
```html
{{ nome }}
{{ idade }}
{{ altura }}
```

---

### Estruturas de controle em templates

* O uso de estruturas de controle permite modificar o comportamento do template de acordo com o valor de uma variável
* As variáveis devem ser passadas para o template através do método `render_template`
* **Sintaxe:** 
```html
{% if condicao %}
    ...
{% elif condicao %}
    ...
{% else %}
    ...
{% endif %}
```

---

### Exemplo de estruturas de controle em templates

```html
{% if idade >= 18 %}
    <p>Seja bem-vindo ao site!</p>
{% else %}
    <p>Este site é apenas para maiores de 18 anos.</p>
{% endif %}
```

---

### Exemplo de estruturas de controle em templates (2)

```html
{% if idade >= 18 %}
    <p>Seja bem-vindo ao site!</p>
{% elif idade >= 16 %}
    <p>Este site é apenas para maiores de 18 anos.</p>
{% else %}
    <p>Este site é apenas para maiores de 16 anos.</p>
{% endif %}
```

---

## Estruturas de repetição em templates
### O laço `for`

```html
{% for item in lista %}
    <p>{{ item }}</p>
{% endfor %}
```	

--

### Exemplo de estruturas de repetição em templates
## O laço `while`

```html
{% set i = 0 %}
{% while i < 10 %}
    <p>{{ i }}</p>
    {% set i = i + 1 %}
{% endwhile %}
```

---

## Exercícios

#### Modifique o código da aplicação para que as páginas do site sejam geradas dinamicamente
1. Crie um template para o menu de navegação do site
2. Crie um template para o rodapé do site
3. Crie um template para a página de contato do site
4. Crie um template para a página de sobre do site
