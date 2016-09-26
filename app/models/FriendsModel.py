
from system.core.model import Model

class FriendsModel(Model):
    def __init__(self):
        super(FriendsModel, self).__init__() 
# registration
    def create_user(self,info):
        print "create_user"
        if 'name' in info and 'alias' in info and 'email' in info and 'date_of_birth' in info and 'password' in info and 'confirm_password' in info:
            name = info['name']
            alias = info['alias']
            email = info['email'].lower()
            date_of_birth = info['date_of_birth']
            password = info['password']
            confirm_password = info['confirm_password']
            errors = []
            if name is None:
                errors.append(('Name cannot be blank','name'))
            if alias is None:
                errors.append(('Alias cannot be blank','alias'))
            if email is None:
                errors.append(('Email cannot be blank','email'))
            elif not EMAIL_REGEX.match(email):
                errors.append(('Please enter valid email','email'))
            if password is None:
                errors.append(('Password cannot be blank','password'))
            if len(password)<8:
                errors.append(('Password has to be at least 8 characters','password'))
            if confirm_password is None:
                errors.append(('Password confirmation cannot be blank','password'))
            if password and confirm_password and password != confirm_password:
                errors.append(('Passwords do not match','password'))

            if errors: 
                return{"status":False, "errors":errors}

            else:
                encrypted_password = self.bcrypt.generate_password_hash(password)
                
                query = "INSERT INTO users (name, alias, email, password, date_of_birth, created_at, updated_at) VALUES (:name, :alias, :email, :password, :date_of_birth, NOW(), NOW())"
                data = {'name':name, 'alias':alias, 'email':email, 'date_of_birth':date_of_birth, 'password':encrypted_password}
                users = self.db.query_db(query,data)
                
                return {"status":True, "user":users}

# Display friend list after login
    def friend_list(self):
        query = "SELECT * FROM users WHERE id=:id"

#show user's profile
    def profile(self):
        query = "SELECT * FROM users WHERE id=:id LIMIT 1"

#delete friend
    def remove_friend(self):
         query ="DELETE from users WHERE friend_id=:friend_id"

#addfriend
    def add_friend(self):
        query="INSERT INTO users (friend_id) VALUES (:friend_id)"



    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """