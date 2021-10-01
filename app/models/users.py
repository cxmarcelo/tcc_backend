import datetime
from app import db, ma


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    crm = db.Column(db.String(20))
    name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, name, crm, user_type):
        self.email = email
        self.password = password
        self.name = name
        self.crm = crm
        self.user_type = user_type


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'password', 'crm', 'user_type', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
