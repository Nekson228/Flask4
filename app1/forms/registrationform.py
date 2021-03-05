from wtforms import SubmitField, IntegerField, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    surname_field = StringField('Фамилия:', validators=[DataRequired()])
    name_field = StringField('Имя:', validators=[DataRequired()])
    age_field = IntegerField('Возраст:', validators=[DataRequired()])
    position_field = StringField('Звание:', validators=[DataRequired()])
    speciality_field = StringField('Должность:', validators=[DataRequired()])
    address_field = StringField('Адресс:', validators=[DataRequired()])
    email_field = EmailField('E-mail:', validators=[DataRequired()])
    password_field = PasswordField('Пароль:', validators=[DataRequired()])
    confirm_password_field = PasswordField('Подтвердите пароль:', validators=[DataRequired(),
                                                                              EqualTo('password_field',
                                                                                      'Пароли должны совадать')])
    submit_field = SubmitField('Регистрация')
