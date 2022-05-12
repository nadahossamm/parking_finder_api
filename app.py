from flask import Flask
import model.model_app as model
import owner_user.owner_app as owner
import driver_user.driver_app as driver
import user.user_app as user
import database.connect_database as db_connection

db = db_connection.connect()
app = Flask(__name__)

@app.route('/find', methods=['POST'])
def find():
    return model.find()

@app.route('/add_garage', methods=['POST'])
def add_garage():
    return owner.create(db)

@app.route('/get_garage', methods=['GET'])
def get_garage():
    return owner.get(db)

@app.route('/update_garage', methods=['POST', 'PUT'])
def update_garage():
    return owner.update(db)

@app.route('/delete_garage', methods=['GET', 'DELETE'])
def delete_garage():
    return owner.delete(db)

@app.route('/show_reviews_garage', methods=['GET'])
def show_reviews_garage():
    return owner.show_reviews_garage(db)

@app.route('/show_reviews_street', methods=['GET'])
def show_reviews_street():
    return owner.show_reviews_street(db)
