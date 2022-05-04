from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model


class Dojo:
    def __init__(self,data):
        self.id = data['id']

        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def create_dojo(cls,data):
        query = 'INSERT INTO dojos(name,created_at,updated_at) VALUES(%(name)s,NOW(),NOW());'

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        return results

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        all_dojos = []

        for row in results:
            all_dojos.append(cls(row))

        return all_dojos

    @classmethod
    def dojo_ninjas(cls,data):

        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;'

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        dojo = cls(results[0])

        for data in results:
            ninja_data = {
                'id' : data['ninjas.id'],
                'first_name' : data['first_name'],
                'last_name' : data['last_name'],
                'age' : data['age'],
                'created_at' : data['ninjas.created_at'],
                'updated_at' : data['ninjas.updated_at']

            }

            ninja_instance = ninja_model.Ninja(ninja_data)

            dojo.ninjas.append(ninja_instance)


        return  dojo
