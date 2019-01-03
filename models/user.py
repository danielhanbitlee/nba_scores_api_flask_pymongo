from db import db


class UserModel:
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.id = user_id

    @classmethod
    def find_by_username(cls, username):
        users = db.users

        doc = users.find({'username': username}, {'_id': 0})
        doc_values = [d.values() for d in doc]

        if doc_values:
            user = cls(*doc_values[0])
        else:
            user = None

        return user
    
    @classmethod
    def find_by_id(cls, user_id):
        users = db.users

        doc = users.find({'user_id': user_id}, {'_id': 0})
        doc_values = [d.values() for d in doc]

        if doc_values:
            user = cls(*doc_values[0])
        else:
            user = None

        return user

    def save_to_db(username, password):
        users = db.users
        users.insert({'username': username, 'password': password})
        user_id = str(list(users.find({'username': username}))[0]['_id'])
        users.update({'username': username}, {"$set": {"user_id": user_id}})
 
