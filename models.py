from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    password = db.Column(db.String(100))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name} Email {self.email}>' 