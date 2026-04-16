from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, DataRequired

class VerificarEmail(FlaskForm):
    email = StringField(
        'email',
        validators=[
            DataRequired(message='O email é obrigatório.'),
            Email(message='Digite um email válido')
        ]
    )