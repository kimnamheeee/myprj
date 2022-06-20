#-*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fcuser(db.Model): 
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key = True)   # 프라이머리키
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))
