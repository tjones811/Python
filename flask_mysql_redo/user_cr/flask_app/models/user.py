from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import faction

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.faction ={} #placeholder for one faction


    @staticmethod
    def validate_user(form_data):
        is_valid = True

        if len(form_data['first_name']) < 2:
            flash('You must provide a longer name')
            is_valid = False

        if not EMAIL_REGEX.match(form_data['email']):
            flash('Please enter a valid email address')
            is_valid = False


        return is_valid

    @classmethod
    def get_all(cls):

        query = 'SELECT * FROM users;'

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
            
        return users

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email,created_at,updated_at,faction_id) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW(),%(faction_id)s)'
        
        result = connectToMySQL('users_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE  id = %(id)s ;'

        result = connectToMySQL('users_schema').query_db(query,data)

        return cls(result[0])


    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s,updated_at = NOW() WHERE id = %(id)s '
        result = connectToMySQL('users_schema').query_db(query,data)
        return result

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
        

    @classmethod
    def get_user_with_faction(cls,data):
        query = 'SELECT * FROM users JOIN factions ON users.faction_id = factions.id WHERE users.id = %(id)s'
        results = connectToMySQL('users_schema').query_db(query,data)


        user = cls(results[0])

        faction_data = {
            'id': results[0]['factions.id'],
            'name': results[0]['name'],
            'level': results[0]['level'],
            'date_created': results[0]['date_created'],
            'created_at': results[0]['factions.created_at'],
            'updated_at': results[0]['factions.updated_at']
        }

        faction_instance = faction.Faction(faction_data)
        user.faction = faction_instance

        return user