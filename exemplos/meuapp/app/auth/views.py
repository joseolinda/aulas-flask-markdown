from flask import render_template, request
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        return 'Formulário enviado'
    
    if form.validate_on_submit():
        # lógica para logar usuário
        pass
    
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # lógica para registrar usuário
        pass
    return render_template('register.html', form=form)
