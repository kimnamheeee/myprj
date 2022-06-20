#-*- coding: utf-8 -*-

from click import password_option
from flask import Flask, render_template, request, redirect, flash, session
from models import db, Fcuser
import os # 경로 지정
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.secret_key = 'my_key'

@app.route('/')
def mainpage(): # 기본
    userid = session.get('userid', None)
    return render_template("index.html", userid=userid)

@app.route('/register', methods=['GET','POST']) # 회원가입
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')

        print(fcuser.userid, fcuser.password)
        db.session.add(fcuser)
        db.session.commit()

        return "가입이 완료되었습니다."

    return render_template("register.html", form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('{} 사용자가 로그인했습니다'.format(form.data.get('userid')))
        session['userid'] = form.data.get('userid')
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('userid', None) # 받았던 세션 삭제
    return redirect('/')

@app.route('/review')
def review():
    return render_template("writereview.html")

@app.route('/post', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        review = request.form.get('writereview')
        value = request.form.get('writereview')
        return redirect("/")
    return render_template("/", value=value)

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  # DB 경로
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'my_key'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all() #DB 생성

    app.run(port=5000, debug=True)
