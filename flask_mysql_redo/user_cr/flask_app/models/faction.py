from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Faction:
    def __init__(self,data):
        self.id = data['id']
        
        self.name = data['name']
        self.level = data['level']
        self.date_created = data['date_created']
        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.users = [] #placeholder/empty list for multiple users


    @classmethod
    def create_new_faction(cls,data):
        query = 'INSERT INTO factions (name,level,date_created,created_at,updated_at) VALUES(%(name)s,%(level)s,%(date_created)s,NOW(),NOW());' 
        results = connectToMySQL('users_schema').query_db(query,data)
        return results

    @classmethod
    def get_all_factions(cls):
        query = 'SELECT * FROM factions;'
        results = connectToMySQL('users_schema').query_db(query)
        
        all_factions = []

        for row in results:
            all_factions.append(cls(row))
            
        return all_factions

    @classmethod
    def get_faction_with_users(cls,data):
        query = '''SELECT * FROM factions
                LEFT JOIN users ON users.faction_id = factions.id
                WHERE factions.id = %(faction_id)s'''
        
        results = connectToMySQL('users_schema').query_db(query,data)
        
        faction = cls(results[0])

        for data in results:
            user_data = {
                'id': data['users.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'created_at': data['users.created_at'],
                'updated_at': data['users.updated_at']
            }

            user_instance = user.User(user_data)

            faction.users.append(user_instance)

        return faction





