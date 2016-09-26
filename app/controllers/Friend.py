
from system.core.controller import *

class Friend(Controller):
    def __init__(self, action):
        super(Friend, self).__init__(action)

        self.load_model('FriendsModel')
        self.db = self._app.db
   
    def index(self):

        return self.load_view('index.html')

    def create(self):
#WHYYYYYYYYYYYYYY
        info = {
        "name": request.form["name"],
        "alias": request.form["alias"],
        "email": request.form["email"],
        "date_of_birth": request.form["date_of_birth"],
        "password": request.form["password"],
        "confirm_password":request.form["confirm_password"]
        }
        create_status = self.models['FriendsModel'].create_user(info)
        if create_status['status'] == True:
            return redirect ('/friends')

        else:
            print "errors"
            for message in create_status['errors']:
                flash(message[1],message[0])
                return redirect ('/')



    def list_of_friends(self):
        return self.load_view('list.html')

    def view_profile(self):
        return self.load_view('profile.html')

    def logout(self):
        session = null
        return redirect('/')






        

