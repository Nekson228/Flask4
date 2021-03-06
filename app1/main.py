from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from app1.data import db_session

from app1.data.jobs import Jobs
from app1.data.users import User

from app1.forms.loginform import LoginForm
from app1.forms.addjobform import AddJobForm
from app1.forms.registrationform import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    team_leaders = []
    for i in range(len(jobs)):
        team_leaders.append(' '.join(db_sess.query(User.surname, User.name).filter(User.id == jobs[i].team_leader)[0]))
    return render_template('jobs.html', jobs=jobs, team_leaders=team_leaders)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = User()
        user.surname = form.surname_field.data
        user.name = form.name_field.data
        user.age = form.age_field.data
        user.position = form.position_field.data
        user.speciality = form.speciality_field.data
        user.address = form.address_field.data
        user.email = form.email_field.data
        user.set_password(form.password_field.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация пользователя', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['POST', 'GET'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = Jobs()
        job.job = form.job_field.data
        job.team_leader = form.team_leader_field.data
        job.collaborators = form.collaborators_field.data
        job.work_size = form.work_size_field.data
        job.is_finished = form.finished_field.data
        session.add(job)
        session.commit()
        return redirect('/')
    return render_template('add_job.html', form=form)


if __name__ == '__main__':
    db_session.global_init('db/mars_explorer.sqlite')
    app.run()
