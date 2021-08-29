import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
#SECRET_KEY = "".join(random.choice(random_str) for i in range(12))
SECRET_KEY = "fkek3o3E49zp"
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/tcc_chagas'
SQLALCHEMY_TRACK_MODIFICATIONS = False
