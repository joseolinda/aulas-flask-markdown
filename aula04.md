---
theme : "night"
transition: "concave"
highlightTheme: "github-dark-dimmed"
slideNumber: true
title: "Aula 04 - Formulários com Flask"
customTheme: "assets/pweb1"

---
<!-- .slide: data-background="#4d7e65" -->
# Programação Web I - Flask
![Flask](/assets/logo-flask.png "Logo do Flask"){width=100px}
## Aula 04 - Formulários com Flask

Prof. José Olinda

---

# Conteúdo

- Formulários HTML
- Criando Formulários com Flask
- Validação de Formulários
- Formulário e Métodos HTTP

---

# Formulários HTML

- Formulários HTML são usados para coletar dados de usuários
- Contém elementos que permitem ao usuário inserir dados
- Os dados são enviados para um servidor para processamento
- O formulário é definido com a tag `<form>`
- Principais atributos:
  - `action`: URL para onde os dados do formulário serão enviados
  - `method`: método HTTP usado para enviar os dados do formulário

---

# Formulários com Flask

- É possível utilizar bibliotecas de terceiros para criar formulários com Flask
- Exemplos:
  - Flask-WTF
  - WTForms
- Inicialmente, vamos criar formulários sem utilizar bibliotecas de terceiros

--

### Passos para criar um formulário

1. Crie um template HTML para o formulário

```html
<form action="{{ url_for('cadastrar')}}" method="POST">
  <label for="nome">Nome completo:</label><br>
  <input type="text" name="nome"><br>
  <label for="email">E-mail:</label><br>
  <input type="email" name="email"><br>
  <label for="senha">Senha:</label><br>
  <input type="password" name="senha"><br>
  <label for="confsenha">Confirme a senha:</label><br>
  <input type="password" name="confsenha"><br>
  <input type="submit" value="Cadastrar Usuário">
</form>

--

2. Crie uma rota para o formulário (opcao 1)

```python
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confsenha = request.form['confsenha']
        return f'Nome: {nome} <br> E-mail: {email} <br> \
            Senha: {senha} <br>Confirmação: {confsenha}'
    return render_template('cadastrar.html')
```

--

2. Crie uma rota para o formulário (opcao 2)

```python
@app.route('/novaconta')
def novaconta():
    return render_template('cadastrar.html')
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    return f'Nome: {nome} <br> E-mail: {email} <br> \
      Senha: {senha} <br>Confirmação: {confsenha}'
```

---

# Validação de Formulários

- Validação de formulários é importante para garantir que os dados inseridos pelo usuário são válidos
- Exemplos de validação:
  - Campos obrigatórios
  - Tamanho mínimo e máximo de campos
  - Formato de campos (e-mail, CPF, etc.)
  - Campos iguais (senha e confirmação de senha)

--

### Validação de Formulários com Flask

- Flask não possui uma biblioteca nativa para validação de formulários
- É possível utilizar bibliotecas de terceiros para validação de formulários
- Também é possível criar validações personalizadas, usando o próprio Python

--

### Validação de Formulários com Flask

- Exemplo de validação de formulário com Flask

```python
    if nome == '':
        return 'O campo nome é obrigatório'
    elif len(nome) < 3:
        return 'O nome deve ter pelo menos 3 caracteres'
    elif email == '':
        return 'O campo e-mail é obrigatório'
    elif senha == '':
        return 'O campo senha é obrigatório'
    elif senha != confsenha:
        return 'As senhas não conferem'
    else:
        return f'Nome: {nome} <br> E-mail: {email} <br> Senha: {senha} \
            <br>Confirmação de senha: {confsenha}'
```

---

# Formulário e Métodos HTTP

- Métodos HTTP são usados para indicar a ação que deve ser executada em um recurso
- Exemplos de métodos HTTP:
  - GET: obter um recurso
  - POST: criar um recurso
  - PUT: atualizar (editar) um recurso
  - DELETE: remover um recurso

--

### Exemplo de aplicação

1. Acesse o repositório de um projeto no GitHub
2. Clique no botão "Fork" para criar uma cópia do projeto
3. Faça alterações e mlhorias no projeto

- Link:
[!CRUD em Flask](https://github.com/joseolinda/crudflask)
