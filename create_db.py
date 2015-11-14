import os
import sqlite3

STATIC_PATH = os.getcwd()
database = STATIC_PATH+'/db/datadump.db'


''' sets up database if it isn't already set up '''
def setup_db():
    if not os.path.exists(database):
        # database doesn't exist yet
        connection = sqlite3.connect('db/chess.db')
        cursor = connection.cursor()

        '''
        TODO - make tables and stuff here
        '''

    else:
        '''
        TODO - make tables and stuff here
        '''


if __name__=='__main__':
    setup_db()
