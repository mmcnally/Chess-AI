import os
import sqlite3

STATIC_PATH = os.getcwd()
database = STATIC_PATH+'/db/datadump.db'


''' sets up database if it isn't already set up '''
def setup_db():
    conn = sqlite3.connect('db/chess.db')
    c = conn.cursor()

    ''' create table if it isn't there '''
    c.execute("CREATE TABLE IF NOT EXISTS Moves(" +
              "Board STRING NOT NULL, " +
              "Move STRING NOT NULL, " +
              "Wins INT NOT NULL, " +
              "TotalSeen INT NOT NULL, " +
              "PRIMARY KEY (Board, Move))")

    ''' create indices for table if they aren't there '''
    c.execute("CREATE INDEX IF NOT EXISTS board_index ON Moves (Board)")
    c.execute("CREATE INDEX IF NOT EXISTS move_index ON Moves (Move)")

def get_connection():
    setup_db()
    return sqlite3.connect('db/chess.db')


if __name__=='__main__':
    setup_db()
