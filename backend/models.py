from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)#must be unique
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self): #all the diff fields on our objs and convert it into python
    #dictionary and then convert it to json which we can pass from our API
        return {
            "id" : self.id,
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "email" : self.email,
            #the above names are written in "camel_case" : use when giving API name and Json names, and the above python var names are in "snake_case"
        }
