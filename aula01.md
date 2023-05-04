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
## Aula 01 - Introdução ao Flask

Prof. José Olinda

---

## Conteúdos


* Por que precisamos de um framework?
* Aprensentando o Flask
* Como instalar o Flask
* Criar uma aplicação básica em Flask
* Criar uma aplicação com rotas em Flask
* Prática: Currículo em Flask

---

<!-- .slide: data-background="#4d7e65" -->

## Por que precisamos de um framework?

* Um framework é um conjunto de ferramentas que facilitam o desenvolvimento de aplicações
* Python é uma linguagem de programação de alto nível, mas não é uma linguagem de programação web (originalmente)
* O Flask é um framework web para Python
* O Flask é um microframework, ou seja, ele não possui muitas funcionalidades, mas é fácil de aprender e usar
* Outras opções: Django, Pyramid, Bottle, Tornado, etc.

---

<!-- .slide: data-background="#fafafa" -->
# Flask
![Flask](/assets/logo-flask.png "Logo do Flask"){width=100px, style="float: right; margin-left: 20px; margin-top: 20px;"}

| Propriedade        | Descrição           |
|--------------------|:--------------------:
| **Linguagem**      | Python              |
| **Criador**        | Armin Ronacher      |
| **Lançamento**     | 1 de abril de 2010  |
| **Última versão**  | 2.2.3 (23 de fevereiro de 2023) |
| **Licença**        | BSD                 |
| **Website**        | https://flask.palletsprojects.com/en/2.2.x/ |
| **Classificação**   | Microframework |

---

## Como instalar o Flask

<code style="font-size: 16px">
Atenção: É necessário ter o Python 3.x e o virtualenv instalado no seu computador e devidamente configurado no path.
</code><br>

1. Teste os requisitos básicos

```bash
# Verificar a versão do Python
python --version

# Verificar a versão do pip
pip --version

# Verificar a versão do virtualenv
virtualenv --version
```

--

2. Configurar ambiente virtual:

```bash
# Criar uma pasta para o projeto
mkdir aula01
cd aula01

# Criar um ambiente virtual
virtualenv venv

# Ativar o ambiente virtual
source venv/bin/activate # Linux
venv\Scripts\activate.bat # Windows
```

--

3. Instalar o Flask

```bash
pip install flask
```	

```python
# Abrir o interpretador do Python
python
# Testar importação do Flask
from flask import Flask
```
<br>
<small style="color: #e7ad52; width: 480px">
<p><i class="fa fa-warning"></i> ATENÇÃO:</p>
O comportamento esperado é que não apareça nenhuma mensagem de erro, pois o Flask foi instalado corretamente. Caso contrário, verifique se o ambiente virtual está ativado e se o Flask foi instalado corretamente.
</small>

---

## Criar uma aplicação básica em Flask

Todo projeto Flask requer uma pasta. Crie uma pasta chamada `aula01` e dentro dela crie um arquivo chamado `app.py`.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
```

--

## Como executar?
#### Opção 1 - Via Flask run

Abra o terminal e execute o comando:

```bash
flask run
```
Agora, no navegador de sua preferência, acesse o endereço http://127.0.0.1:5000

<br>
<small style="color: #e7ad52; width: 480px">
<p><i class="fa fa-warning"></i> ATENÇÃO:</p>
Geralmente, o Flask criar um servidor local no endereço 127.0.0.1:5000 ou localhost:5000.
Para encerrar o servidor, pressione Ctrl+C.
</small>

--

## Como executar?
#### Opção 2 - Via Python

Modifique o arquivo `app.py` para:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
```

--

## Como executar?
#### Opção 2 - Via Python (continuação)

Abra o terminal e execute o comando:

```bash
python app.py
```
Agora, no navegador de sua preferência, acesse o endereço http://127.0.0.1:5000

<br>
<small style="color: #e7ad52; width: 480px">
<p><i class="fa fa-warning"></i> ATENÇÃO:</p>
A porta do seu servidor local pode variar, caso haja uma outra aplicação rodando na mesma porta. No terminal, após executar o comando, veja qual endereço e porta o seu sevidor está em execução. Para encerrar o servidor, pressione Ctrl+C.
</small>

---

## Outras formas de executar a sua aplicação web
Como usar o comando `flask run`

1. Quando sua aplicação não se chamar `app.py` ou `wgsi.py`, será necessário informar qual o arquivo que representa sua aplicação Flask. Para isso, use o comando:

```bash
# flask --app <nome_do_arquivo> run
flask --app hello.py run
```

--

2. Quando sua aplicação não estiver no diretório atual, será necessário informar o caminho para o arquivo que representa sua aplicação Flask. Para isso, use o comando:

```bash
# flask --app <caminho_do_arquivo> run
flask --app /home/user/aula01/hello.py run
```

--

## Outras formas de executar a sua aplicação web
Como usar o comando `app.run()`

1. Quando sua aplicação for iniciada pelo próprio aquivo, usandos o comando `python <nome_do_arquivo>`. Dentro do arquivo, você deve chamar o método `app.run()` da sua aplicação Flask. Para isso, use o comando:

```bash
# no terminal
python hello.py
```

```python
# no arquivo hello.py
if __name__ == '__main__':
    app.run(debug=True)
```

--

2. Possíveis parâmetros para o método `app.run()`:
<br>
<br>


| Parâmetro  | Obrigatório  | Tipo  | Descrição  |
|------------|:------------:|:-----:|:-----------|
| host       | Não          | str   | O endereço IP que o servidor web deve escutar. O padrão é 127.0.0.1 |
| port       | Não          | int   | O número da porta que o servidor web deve escutar. O padrão é 5000 |
| debug      | Não          | bool  | Se for passado, habilita ou desabilita o modo de debug. O padrão é False |
| load_dotenv| Não          | bool  | Carrega os arquivos .env e .flaskenv mais próximos para definir as variáveis de ambiente. Também altera o diretório de trabalho para o diretório que contém o primeiro arquivo encontrado. O padrão é False |
| options    | Não          | Any   | As opções a serem encaminhadas para o servidor Werkzeug subjacente. |

--

3. Podemos passar o ip 0.0.0.0 para o parâmetro `host` para que o servidor web escute todas as interfaces de rede. Isto significa que seu site/aplicação web será acessível a partir de qualquer outra máquina na rede local. Para isso, use o comando:
<br>
<br>
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0')
```
<br>
<p style="text-align: left">
Sabendo o IP do seu computador, outro computador na mesma rede pode acessar o seu site/aplicação web através do endereço http://<seu_ip>:5000</p>

---

## Rotas

<br>

* Chamamos de rota o caminho que o usuário percorre para acessar uma página ou recurso (URL). No Flask, as rotas são definidas através do decorator `@app.route()`.

* `decorators` ou decoradores são funções que envolvem outras funções e são usados para modificar o comportamento de uma função sem a necessidade de alterá-la explicitamente.

* Usamos o decorator `@app.route()` para informar ao Flask qual URL deve acionar a função.

--

### URL

* URL é o endereço de um recurso disponível em uma rede, como a internet. A URL é uma sigla para o termo em inglês Uniform Resource Locator, que significa Localizador Padrão de Recursos.

| url                    | URL Base     | Rota/Recurso |
|------------------------|:------------:|:------------:|
| google.com.br | google.com.br | / |
| google.com/maps | google.com | /maps |
| google.com/photos | google.com | /photos |
| ifce.edu.br/cedro | ifce.edu.br | /cedro |

--

## `@app.route(<parametros>)`

* Os parâmetros do decorator `@app.route()` são strings que representam a URL que será acessada pelo usuário.

* Exemplos:

```python
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'Sobre Mim'
```

---

## Criando uma aplicação web com Flask

1. Crie um diretório chamado `meuapp` e abra-o no seu editor de código.

2. Crie um arquivo chamado `app.py` e adicione o seguinte código:

<pre><code data-line-numbers="1|2|3-5|7-9|11-13|15-17|19-20">from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Bem-vindo à nossa loja online!'

@app.route('/produtos')
def produtos():
    return 'Aqui estão nossos produtos disponíveis.'

@app.route('/carrinho')
def carrinho():
    return 'Seu carrinho de compras está vazio.'

@app.route('/checkout')
def checkout():
    return 'Obrigado por comprar conosco!'

if __name__ == '__main__':
    app.run()
</pre></code>

---

## Prática
### Crie uma aplicação web com Flask

* Crie um currículo online com as seguintes rotas:
    * `/` - página inicial
    * `/sobre` - página sobre você
    * `/experiencia` - página com sua experiência profissional
    * `/formacao` - página com sua formação acadêmica
    * `/contato` - página com seus contatos

* Cada página deve conter um título e um texto de apresentação.
* A página inicial deve conter um link para cada página do currículo.

---

# Dúvidas?

### jose.olinda@ifce.edu.br