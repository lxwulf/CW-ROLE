"""
Script for initialization of the database
structure in postgresql for nextcloud
"""

__author__ = 'Officer K'
__version__ = 3.3

import sys
import psycopg2

CONNECTION = None
LOG = '\033[92m' + '[   OK   ] ' + '\033[0m'
LOGWARN = '\033[93m' + '[  WARN  ] ' + '\033[0m'
LOGERR = '\033[91m' + '[  ERROR ] ' + '\033[0m'
LOGINFO = '\033[96m' + '[  INFO  ] ' + '\033[0m'

try:
    CONNECTION = psycopg2.connect("user='postgres' dbname=template1 \
                                  host='192.168.1.101' port='5432'")
    print(LOG + 'Database connected.')
except ValueError():
    print(LOGERR + 'No connection to the database')
    sys.exit()

if CONNECTION is not None:
    CONNECTION.autocommit = True
    agent = CONNECTION.cursor()
    agent.execute('SELECT datname FROM pg_database')
    LIST_DATABASES = agent.fetchall()
    agent.execute('SELECT usename FROM pg_catalog.pg_user')
    LIST_USERNAMES = agent.fetchall()
    DB_USER = 'ncadmin'                                         # Set the admin user of the database
    DB_NAME = 'ncdb'                                            # Set the name of the database
    DB_PW = 'YourSecurePassword'                                # Set your password for the database
else:
    sys.exit()

if (DB_NAME,) and (DB_USER,) in (LIST_USERNAMES):
    print(LOGINFO + f'Database {DB_NAME} already exist.')
    print(LOGINFO + f'User {DB_USER} already exist.')

elif (DB_NAME,) in (LIST_DATABASES):                            # user does not exist
    print(LOGWARN + f'Database {DB_NAME} already exist.')
    print(LOGERR + f'User {DB_USER} does not exist.')
    print(LOG + f'Creating user {DB_USER} with owner permissions and fully access to ' \
                  f'database {DB_NAME}.')
    agent.execute(f'''CREATE USER {DB_USER} WITH PASSWORD '{DB_PW}';
                    ALTER DATABASE {DB_NAME} OWNER to {DB_USER};
                    GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};
                  ''')
    print(LOGINFO + 'Done.')
elif (DB_USER,) in (LIST_USERNAMES):                             # database does not exist
    print(LOGWARN + f'User {DB_USER} does already exist.')
    print(LOGERR + f'Database {DB_NAME} does not exist.')
    agent.execute(f'CREATE DATABASE {DB_NAME} TEMPLATE template0 ENCODING UNICODE')
    print(LOG + f'Created database {DB_NAME}.')
    print(LOG + f'Grant database user {DB_USER} all privileges on database {DB_NAME}.')
    agent.execute(f'''ALTER DATABASE {DB_NAME} OWNER to {DB_USER};
                    GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};
                  ''')
    print(LOGINFO + 'Done')
else:                                                             # database and user does not exist
    print(LOGWARN + f'Database {DB_NAME} and {DB_USER} user does not exist')
    agent.execute(f'CREATE DATABASE {DB_NAME} TEMPLATE template0 ENCODING UNICODE')
    agent.execute(f'''CREATE USER {DB_USER} WITH PASSWORD '{DB_PW}';
                    ALTER DATABASE {DB_NAME} OWNER to {DB_USER};
                    GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};
                  ''')
    print(LOG + f'Database {DB_NAME} with {DB_USER} successfully created.')
    print(LOGINFO + 'Done')

CONNECTION.close()
