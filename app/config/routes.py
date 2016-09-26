
from system.core.router import routes


routes['default_controller'] = 'Friend'
routes['POST']['/create']='Friend#create'
routes['/friends']='Friend#list_of_friends'
routes['/user/id']='Friend#view_profile'
