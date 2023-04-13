from sqlalchemy import create_engine
from faker import Faker

engine = create_engine('postgresql://root:root@localhost:5432/postgres')
connection = engine.connect()

# Create
#connection.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
#connection.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

fake = Faker()

id_User = fake.pyint(min_value = 1, max_value = 100)
firstname = fake.first_name()
lastname = fake.last_name()
age = fake.pyint(min_value = 18, max_value = 85)
email = fake.email()
job = fake.job()

# id_Application = fake.pyint(min_value = 1, max_value = 100)
# appname = fake.name()
# username = fake.user_name()
# lastconnection = fake.date()

# for i in range (20):
#     id_User = fake.pyint(min_value = 1, max_value = 100)
#     firstname = fake.first_name()
#     lastname = fake.last_name()
#     age = fake.pyint(min_value = 18, max_value = 85)
#     email = fake.email()
#     job = fake.job()
    
#     id_Application = fake.pyint(min_value = 1, max_value = 100)
#     appname = fake.name()
#     username = fake.user_name()
#     lastconnection = fake.date()

#     User = []
#     Application = []

#     User.append(id_User)
#     User.append(firstname)
#     User.append(lastname)
#     User.append(age)
#     User.append(email)
#     User.append(job)

#     Application.append(id_Application)
#     Application.append(appname)
#     Application.append(username)
#     Application.append(lastconnection)




    
    

  

















