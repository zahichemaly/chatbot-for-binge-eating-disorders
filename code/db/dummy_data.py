import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def add_dummy_users():
    # adding dummy users
    c.execute("INSERT INTO Users VALUES (552993400, 'maria', 31, 'F')")
    conn.commit()


def add_dummy_crisis():
    # adding dummy crisis linked to users
    c.execute("INSERT INTO Crisis VALUES (NULL,'27/07/2016','11:43',120,'home', 0 ,'pizza,burger,fries', 552993400)")
    c.execute("INSERT INTO Crisis VALUES (NULL,'07/08/2018','06:11',20,'work', 1 ,'donuts,fries,cola', 552993400)")
    c.execute("INSERT INTO Crisis VALUES (NULL,'01/01/2015','03:15',80,'park', 0 ,'pizza,icecream', 552993400)")
    c.execute("INSERT INTO Crisis VALUES (NULL,'22/02/2018','20:30',15,'gym', 1 ,'pizza,icecream', 552993400)")
    conn.commit()

def add_dummy_profiles():
    # adding dummy profiles linked to crisis
    c.execute("INSERT INTO Profiles VALUES (NULL, 'B', 'playing the guitar', 'happy', 'dogs', 552993400, 1 )")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'A', 'listening to music', 'sad', 'boyfriend', 552993400, 1)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'B', 'studying', 'stressed', 'exams', 552993400, 2)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'A', sleeping', 'relaxed', 'nature', 552993400, 2)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'B', 'working', 'depressed', 'beach', 552993400, 3)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'A', eating', 'angry', 'wife', 552993400, 3)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'B', 'running', 'happy', 'trees', 552993400, 4)")
    c.execute("INSERT INTO Profiles VALUES (NULL, 'A', 'swiming', 'tired', 'ocean', 552993400, 4)")
    conn.commit()

def add_dummy_cards():
    c.execute("INSERT INTO Emcards VALUES (NULL, 'take a shower', '13:45', 60, 552993400)")
    c.execute("INSERT INTO Emcards VALUES (NULL, 'watch a movie', '6:10', 120, 552993400)")
    conn.commit()

if __name__ == '__main__':
    add_dummy_users()
    add_dummy_crisis()
    add_dummy_profiles()
    add_dummy_cards()
    conn.close()