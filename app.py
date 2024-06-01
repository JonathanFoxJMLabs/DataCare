from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

# Routes for demonstration purposes
@app.route('/add_person', methods=['POST'])
def add_person():
    data = request.get_json()
    new_person = Person(
        P_FName=data['P_FName'],
        P_MName=data.get('P_MName'),
        P_LName=data['P_LName'],
        Age=data['Age'],
        Person_Type=data['Person_Type']
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person added successfully"}), 201

@app.route('/get_people', methods=['GET'])
def get_people():
    people = Person.query.all()
    result = []
    for person in people:
        person_data = {
            'P_ID': person.P_ID,
            'P_FName': person.P_FName,
            'P_MName': person.P_MName,
            'P_LName': person.P_LName,
            'Age': person.Age,
            'Person_Type': person.Person_Type
        }
        result.append(person_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
