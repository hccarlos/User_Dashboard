""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'(.*([A-Z]+).*([0-9]+).*)|(.*([0-9]+).*([A-Z]+).*)')

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()

    # validate registration data - helper function
    def data_is_valid(self, creation_data):
        allOK = True
        errors = []

        if 'email' in creation_data:
            temp_email = creation_data['email']
            if len(temp_email) < 1:
                errors.append("Email cannot be blank!")
                allOK = False
            if not EMAIL_REGEX.match(temp_email):
                errors.append("Invalid Email Address!")
                allOK = False

        if 'first_name' in creation_data:
            temp_fname = creation_data['first_name']
            if len(temp_fname) < 1:
                errors.append("First Name cannot be blank!")
                allOK = False
            if not temp_fname.isalpha():
                errors.append("Invalid First Name! Cannot contain numbers")
                allOK = False
        
        if 'last_name' in creation_data:
            temp_lname = creation_data['last_name']
            if len(temp_lname) < 1:
                errors.append("Last Name cannot be blank!")
                allOK = False
            if not temp_lname.isalpha():
                errors.append("Invalid Last Name! Cannot contain numbers")
                allOK = False

        if 'password' in creation_data:
            temp_pass = creation_data['password']
            temp_pass2 = creation_data['confirm_password']
            if len(temp_pass) < 1:
                errors.append("Password cannot be blank!")
                allOK = False
            if len(temp_pass) < 8:
                errors.append("Password should be more than 8 characters!")
                allOK = False
            if not PASS_REGEX.match(temp_pass):
                errors.append("Invalid Password! Must have 1 uppercase letter and 1 numeric value")
                allOK = False
            if temp_pass != temp_pass2:
                errors.append("Password and confirmation must match")
                allOK = False
        return allOK

    # validate login. If not error, returns false. Else returns user data
    def validate_login(self, login_data):
        # extract data passed
        email = login_data['email']
        password = login_data['password']
        # pull that password data from DB based on email, and match against password
        if (email > 0) and (password > 0):
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email': email}
            user = self.db.query_db(query, data)
            print user
            # if no user with that email found
            if not user:
                print 'no such user'
                return False
            # if password matches, then return the user
            if self.bcrypt.check_password_hash(user[0]['password'], password):
                return user[0]
            # or if password doesn't match
            else:
                return False
        else:
            return False


    # select all users
    def get_all_data(self):
        return self.db.query_db("SELECT * FROM users")

    # select single user. Returns one user's data
    def get_data_by_user_id(self, user_id):
        print 'password enter success'
        query = "SELECT * FROM users WHERE id = :user_id"
        data = {
                'user_id': user_id
        }
        one_user = self.db.query_db(query, data)
        return one_user
    # insert user (after validation)
    def create_user(self, creation_data):
        if data_is_valid(creation_data):
            if get_all_data() == []:
                user_level = 'admin'
            else:
                user_level = 'normal'
            hash_pw = self.bcrypt.generate_password_hash(creation_data['password'])
            query = "INSERT INTO users (first_name, last_name, email, password, description, user_level, created_at, updated_at) VALUES (:fname, :lname, :email, :hpass, :description, :user_level, NOW(), NOW())"
            data = {'fname': creation_data['first_name'],
                    'lname': creation_data['last_name'],
                    'hpass': hash_pw,
                    'description': creation_data['description'],
                    'email': creation_data['email'],
                    'user_level': user_level
            }
            inserted_user = self.db.query_db(query, data)
            return {"status": True, "inserted_user": inserted_user}
        else:
            return {"status": False}

    # update user (after validation)
    def update_user(self, update_data):
        if data_is_valid(update_data):
            # update password only
            if 'password' in update_data:
                hash_pw = self.bcrypt.generate_password_hash(update_data['password'])
                query = "UPDATE users SET password=:password WHERE id = :user_id"
                data = {'password': hash_pw, 'user_id': update_data['id']}
                self.db.query_db(query, data)
            # update email, firstname, and last name only
            if 'email' in update_data:
                query = "UPDATE users SET email=:email, first_name=:first_name, last_name=:last_name WHERE id = :user_id"
                data = {
                        'email': update_data['email'],
                        'first_name': update_data['first_name'],
                        'last_name': update_data['last_name'],
                        'user_id': update_data['id']
                        }
                self.db.query_db(query, data)
            # update description only
            if 'description' in update_data:
                query = "UPDATE users SET description=:description WHERE id = :user_id"
                data = {'description': update_data['description'], 'user_id': update_data['id']}
                self.db.query_db(query, data)
            return True
        else:
            return False
    # remove user
    def delete_user(self, user_id):
      query = "DELETE FROM users WHERE id = :user_id"
      data = { "user_id": user_id }
      return self.db.query_db(query, data)


