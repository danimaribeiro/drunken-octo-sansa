#coding=utf-8
from flask.ext.login import UserMixin

class User(UserMixin):
    def __init__(self, iden, nome, email, senha):
        self.id = iden
        self.nome = nome
        self.email = email
        self.senha = senha

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Usuário %r>' % self.nome
