# Statement for enabling the development environment
DEBUG = True
'''
DEBUG: setting this to True activates the debug mode on the app.
This allows us to use the Flask debugger in case of an unhandled
exception, and also automatically reloads the application when it
is updated. It should however always be set to False in production.
It defaults to False.
'''

#SQLALCHEMY_ECHO = True
'''
SQLALCHEMY_ECHO: setting this to True helps us with debugging by
allowing SQLAlchemy to log errors.
'''

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# creates database in the current folder
#abspath-> absolute path function
#print(BASE_DIR)-> prints the path of current directory
#some constants get declared in the file :- __name__ __file__(current file name)


# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/bookmyshow_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#joins the path with app.db
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
