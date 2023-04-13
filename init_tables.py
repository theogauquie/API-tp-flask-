from run_sql import *

def __init_User__(self, firstname, lastname, age, email, job):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.email = email
    self.job = job

def __init_Application__(self, id, appname, username, lastconnection, user_id):
    self.id = id
    self.appname= appname
    self.username = username
    self.user_id = user_id

print(__init_Application__('User', id_User, firstname, lastname, age, email, job))

