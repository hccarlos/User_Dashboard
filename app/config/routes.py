"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
# Sessions Controller
routes['default_controller'] = 'Sessions'
routes['GET']['/session/signin'] = 'Sessions#signin' # display sign in page
routes['POST']['/session/validate'] = 'Sessions#validate' # run login validation
routes['GET']['/session/register'] = 'Sessions#register' # display register page
routes['POST']['/session/registration'] = 'Sessions#registration' # insert registration data into model

# Dashboards Controller
routes['GET']['/dashboard/<string:user_level>'] = 'Dashboards' # display dashboard, depending on user level
routes['GET']['/dashboard/users/new'] = 'Dashboards#new'
routes['POST']['/dashboard/users/create'] = 'Dashboards#create'
routes['GET']['/dashboard/users/editprofile/<int:user_id>'] = 'Dashboards#editprofile'
routes['POST']['/dashboard/users/updateprofile/<int:user_id>'] = 'Dashboards#updateprofile'
routes['GET']['/dashboard/users/edituser/<int:user_id>'] = 'Dashboards#edituser'
routes['POST']['/dashboard/users/updateuser/<int:user_id>'] = 'Dashboards#updateuser'
routes['GET']['/dashboard/users/remove/<int:user_id>'] = 'Dashboards#remove'

# Walls Controller
routes['GET']['/wall/show/<id:user_id>'] = 'Walls#show'
routes['POST']['/wall/postmessage'] = 'Walls#postmessage'
routes['POST']['/wall/postcomment'] = 'Walls#postcomment'

"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
