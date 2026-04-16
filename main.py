from flask import Flask, render_template, flash, redirect, url_for
from forms import VerificarEmail
from enviar_email import enviar_email_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'F7x@L9q#V2m!Zr8$Wp4^Ts6&Hy1*Kd3%Nb5Qa0R'

@app.route('/', methods=['GET', 'POST'])
def index():
    form_email = VerificarEmail()

    if form_email.validate_on_submit():
        enviar_email_user(form_email.email.data)
        flash(f'Email enviado para {form_email.email.data}! Por favor cheque a sua caixa de entrada do Gmail.')
        return redirect(url_for('index'))

    return render_template('index.html', form=form_email)

if __name__ == '__main__':
    app.run(debug=True)
