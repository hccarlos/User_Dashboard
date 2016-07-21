""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class MessageModel(Model):
    def __init__(self):
        super(MessageModel, self).__init__()

    # select all messages
    def get_all_messages(self):
        query = "SELECT messages.id as messageID, messages.message, messages.updated_at as msgPostDate, messages.parent_id, users.first_name, users.last_name FROM messages LEFT JOIN users ON messages.user_id = users.id ORDER BY messages.parent_id DESC, messages.created_at ASC"
        return self.db.query_db(query)

    # select single
    def get_message_by_id(self, message_id):
        pass

    # insert message or comment (since they're same table)
    def insert_message(self, message_data):
        if(message_data['type'] == 'message'):
            
            fk_query = "SET FOREIGN_KEY_CHECKS=0"
            self.db.query_db(fk_query)

            query = "INSERT INTO messages (message, created_at, updated_at, user_id, parent_id) VALUES (:message, NOW(), NOW(), :user_id, :parent_id)"
            data = {'message': message_data['message'],
                    'user_id': message_data['user_id'],
                    'parent_id': None,
                    }
            inserted_user_id = self.db.query_db(query, data)
            
            query = "UPDATE messages SET parent_id=:parent_id WHERE id = :user_id"
            data = {'parent_id': inserted_user_id, 'user_id': inserted_user_id}

            fk_query = "SET FOREIGN_KEY_CHECKS=1"
            self.db.query_db(fk_query)

        elif(message_data['type'] == 'comment'):
            query = "INSERT INTO messages (message, created_at, updated_at, user_id, parent_id) VALUES (:message, NOW(), NOW(), :user_id, :parent_id)"
            data = {'message': message_data['message'],
                    'user_id': message_data['user_id'],
                    'parent_id': message_data['parent_id'],
                    }
            inserted_user_id = self.db.query_db(query, data)

    # update entry
    def update_message(self):
        pass

    # remove entry
    def delete_message(self):
        pass