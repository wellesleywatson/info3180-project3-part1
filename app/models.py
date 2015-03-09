from . import db

class Profile_db(db.Model):
    userid = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(35))
    sex = db.Column(db.String(6))
    age = db.Column(db.Integer)
    prof_add = db.Column(db.Date)
    high_score = db.Column(db.Integer)
    tdollars = db.Column(db.Integer)
    image = db.Column(db.String(80))
    confirmation_code = db.Column(db.String(50))
    confirmation_status = db.Column(db.String(15))
    confirmation_date = db.Column(db.Date)
    
    
    
    
    
    
    
    def __init__(self, userid, username, firstname, lastname, email, sex, age, prof_add, high_score, tdollars, image, confirmation_code, confirmation_status, confirmation_date ):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.sex = sex
        self.age = age
        self.prof_add = prof_add
        self.high_score = high_score
        self.tdollars = tdollars
        self.image = image
        self.confirmation_code = confirmation_code
        self.confirmation_status = confirmation_status
        self.confirmation_date = confirmation_date 
        

    def __repr__(self):
        return '<Profile %r %r>' % (self.firstname, self.lastname)