#create
#- first_name
#- last_name
#- email
# when creating API, we have a server, that's running the API. 
# here, the server is something like "localhost : 5000" , which can be called as domain or URL
# if localhost:5000/home , then endpoint is "home"
# next is we will hit the endpoint only when submit the request to the endpoint
# Request : anything we send something to the server, in our case, API
# request has a type : GET, POST, PUT, PATCH , DELETE
# after type, there is the json data, which are information that come alongside of the request. 
# after that, backend is going to send the response, 
# response contain status : 200 (success), 404 (not found), 400 (bad request), 403 (forbitten or unauthorize)
# response can return json : which contain how the request was successful or some info like this
from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts",methods=["GET"])#decorator
def get_contacts():
    contacts = Contact.query.all() #user flask ... to the alchemy which is ORM, to get all the context that exists inside of the contact database
    #these contacts are python objects so can't return those from code
    #so need to return those in json code
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
    
    new_contact = Contact(first_name=first_name,last_name=last_name,email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e: #The except Exception as e syntax is used to catch any exception that inherits from Python's base Exception class. This means it will catch all types of exceptions, not just specific ones.
#the caught exception is stored in the variable e.
        return jsonify({"message": str(e)}),400 #creates a JSON response with a dictionary containing a single key "message" and the exception's message as its value.
#str(e) converts the exception object to its string representation, which usually includes a description of the error that occurred.
#The 400 after the comma is the HTTP status code for "Bad Request". This status code indicates that the server cannot process the request due to a client error (e.g., invalid data or a constraint violation in the database).
    return jsonify({"message":"User created!"}),201

#Update
#need to know what kind of contact we are updating
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)#contact 11

    if not contact : 
        return jsonify({"message": "User not found"})

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name) #looking for the key "firstname" inside dictionary "data", if found, then returns to us that value
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()#contact 11 already exited, it already added in the session, can just commit so that it change permanently

    return jsonify({"message": "User Updated"}), 200

#Delete
@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)#contact 11

    if not contact : 
        return jsonify({"message": "User not found"})

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200

#run flask app
if __name__ == "__main__":
    with app.app_context():#
        db.create_all()# create all the the different models that we have defined in our database
    
    app.run(debug=True)
#which me if you actually this "main.py", then execute the codes which is inside of app, 
