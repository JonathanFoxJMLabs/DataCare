from app import db

class Person(db.Model):
    __tablename__ = 'person'
    
    P_ID = db.Column(db.Integer, primary_key=True)
    P_FName = db.Column(db.String, nullable=False)
    P_MName = db.Column(db.String, nullable=True)
    P_LName = db.Column(db.String, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Person_Type = db.Column(db.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': Person_Type
    }
