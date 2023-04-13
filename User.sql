class User(db.Model):
    __tableame__ = 'User'
    id = db.COLUMN(db.integer, PRIMARY = true)
    firstname = db.COLUMN(db.string(15))
    lastname = db.COLUMN(db.string(20))
    age = db.COLUMN(db.integer)
    email = db.COLUMN(db.string(50))
    job = db.COLUMN(db.string(50))

class Application(db.Model):
    __tableame__ = 'Application'
    id = db.COLUMN(db.integer, PRIMARY = true)
    appname = db.COLUMN(db.string(50))
    username = db.COLUMN(db.string(20))
    lasconnetion = db.COLUMN(db.DateTime, default = datetime.datetime.now)
    user_id = db.COLUMN(db.integer, FOREIGN('user_id'))


