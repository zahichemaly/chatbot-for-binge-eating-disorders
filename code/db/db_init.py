import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_tables():
    # creating Table "Users" with name, age, gender
    c.execute('''CREATE TABLE Users
             (UID INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER NOT NULL,
             gender CHAR(1) NOT NULL)''')
             # CHAR(1) stores 1 character (M or F)

    # creating Table "Crisis" with foreign key UserID referencing UID of Table "Users"
    # 1 to many relationship (1 user can have multiple crisis)
    c.execute('''CREATE TABLE Crisis
             (CID INTEGER PRIMARY KEY AUTOINCREMENT,
			 date DATE,
             time TEXT,
             duration INTEGER,
             location TEXT,
             alone INTEGER,
             food TEXT,
             userID INTEGER,
             FOREIGN KEY(userID) REFERENCES Users(UID))''')
             
    c.execute('''CREATE TABLE Profiles
             (PID INTEGER PRIMARY KEY AUTOINCREMENT,
             context CHAR(1) NOT NULL,
			 activity TEXT,
			 mood TEXT,
			 thoughts TEXT,
             userID INTEGER,
             crisisID INTEGER,
             FOREIGN KEY(userID) REFERENCES Users(UID)
             FOREIGN KEY(crisisID) REFERENCES Crisis(CID))''')

    # creating Table "Emergency Cards" with foreign key userID referencing UID of Table "Users"
    # 1 to many relationship (1 user can have multiple emergency cards)
    c.execute('''CREATE TABLE Emcards
             (EID INTEGER PRIMARY KEY AUTOINCREMENT,
             activity TEXT,
             time DATETIME,
             duration INTEGER,
             userID INTEGER,
             FOREIGN KEY(userID) REFERENCES Users(UID))''')
    conn.commit()

if __name__ == '__main__':
    create_tables()

