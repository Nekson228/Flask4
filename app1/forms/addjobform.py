from wtforms import BooleanField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class AddJobForm(FlaskForm):
    job_field = StringField('Название работы', validators=[DataRequired()])
    team_leader_field = IntegerField('ID лидера команды', validators=[DataRequired()])
    collaborators_field = StringField('ID работников', validators=[DataRequired()])
    work_size_field = IntegerField('Время выполнения работы', validators=[DataRequired()])
    finished_field = BooleanField('Работа выполнена?', validators=[DataRequired()])
    submit_field = SubmitField('Добавить работу')
