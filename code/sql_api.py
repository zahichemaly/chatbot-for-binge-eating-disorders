import os
import sqlite3 as sql
from user import *
from datetime import datetime
from datetime import timedelta

from telegram_channel import *

dir = os.getcwd() + '/db/database.db'

class SQL_API:
    def __init__(self):
        # get session object from telegram_channel (contains sender_id)
        self.session = session
        self.profiles = {}

    def get_user(self, sender_id):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("SELECT * FROM Users WHERE UID = " + str(sender_id))
        conn.commit()
        u = c.fetchone()
        conn.close()
        # set current user if found
        if u is not None:
            return User(u[0], u[1], u[2], u[3])
        else:
            return None

    def insert_user(self, sender_id, name, age, gender):
        conn = sql.connect(dir)
        c = conn.cursor()
        # get sender_id from telegram
        c.execute("INSERT INTO Users VALUES (" + str(sender_id) + ", '" + name + "'," + str(age) + ",'" + gender + "')")
        conn.commit()
        conn.close()

    def insert_crisis(self, sender_id, date, time, duration, location, is_alone, food):
        conn = sql.connect(dir)
        c = conn.cursor()
        command = "INSERT INTO Crisis VALUES (NULL,'" + date + "', '" + time + "', " + str(duration) + ", '" + location + "'," \
        "" + str(is_alone) + "," + food + ", " + str(sender_id) + ")"
        try:
            c.execute(command)
            c.execute("SELECT last_insert_rowid()")  
            conn.commit()
            id = c.fetchall()[0][0]
            conn.close()
            return Crisis(id, date, time, duration, location, is_alone, food)
        except:
            return None

    def insert_profile(self, sender_id, context, activity, mood, thoughts):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("INSERT INTO Profiles VALUES (NULL, '" + context + "', '" + activity + "', '" + mood + "', '" + thoughts + "'," + str(sender_id) + ", NULL)")
        conn.commit()
        conn.close()

    def update_profile(self, sender_id, crisisID):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("UPDATE Profiles SET crisisID = " + str(crisisID) + " WHERE userID = " + str(sender_id))
        conn.commit()
        conn.close()

    def get_profiles(self, crisis_id):
        conn = sql.connect(dir)
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Profiles WHERE crisisID = " + str(crisis_id))
            conn.commit()
            f = c.fetchall()
            conn.close()
            profiles = []
            i = 0
            while (i < len(f)):
                profiles.append(Profile(f[i][0],f[i][1],f[i][2],f[i][3],f[i][4]))
                i += 1
        except:
               profiles = None
        return profiles


    def insert_emcard(self, sender_id, activity, time = None, duration = None):
        crisisList = self.get_crisis(sender_id)
        if crisisList is None:
            return None
        else:
            # get last crisis from list
            crisis = crisisList[-1]
        if time is None and duration is None:
            # get time and duration from current crisis
            date_str = crisis.date + " " + crisis.time
            format_str = "%d/%m/%Y %H:%M"
            d = datetime.strptime(date_str, format_str)
            # substracting 10 minutes from current time
            d -= timedelta(minutes = 10)
            time = d.strftime("%H:%M")
            duration = crisis.get_duration() + 10

        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("INSERT INTO Emcards VALUES (NULL, '" + activity + "', '" + time + "', " + str(duration) + "," + str(sender_id) + ")")
        c.execute("SELECT last_insert_rowid()")  
        conn.commit()
        id = c.fetchall()[0][0]
        conn.close()
        return Emcard(id, activity, time, duration)

    def get_emcards(self, sender_id):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("SELECT * FROM Emcards WHERE userID = " + str(sender_id))
        conn.commit()
        f = c.fetchall()
        conn.close()
        try:
            cards = []
            i = 0
            while (i < len(f)):
                cards.append(Emcard(f[i][0], f[i][1], f[i][2], f[i][3]))
                i += 1
        except:
               cards = None
        return cards

    def delete_emcard(self, card_id):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("DELETE FROM Emcards WHERE EID = " + str(card_id))
        conn.commit()
        conn.close()

    def get_crisis(self, sender_id):
        conn = sql.connect(dir)
        c = conn.cursor()
        c.execute("SELECT * FROM Crisis WHERE userID = " + str(sender_id))
        conn.commit()
        f = c.fetchall()
        conn.close()
        try:
            crisis = []
            i = 0
            while (i < len(f)):
                # id date time duration location is_alone food
                food = (f[i][6]).split(',')
                crisis.append(Crisis(f[i][0], f[i][1], f[i][2], f[i][3], f[i][4], f[i][5], food))
                i += 1
        except:
               crisis = None
        return crisis

    def fill_profiles(self, CID):
        profiles = {}
        conn = sql.connect(dir)
        c = conn.cursor()
        c = conn.cursor()
        c.execute("SELECT * FROM Profiles WHERE crisisID = " + str(CID))
        conn.commit()
        # list of 2 tuples (Profile Before and After)
        f = c.fetchall()
        profiles = {}
        try:
            profiles['BEFORE'] = Profile(f[0][0], f[0][1], f[0][2], f[0][3], f[0][4])
            profiles['AFTER'] = Profile(f[1][0], f[1][1], f[1][2], f[1][3], f[1][4])
            conn.close()
        except:
            conn.close()
        return profiles

    def list_to_str(self,list_slot):
        if list_slot is None:
            return "NULL"
        else:
            # converting list to string
            list_str = ','.join(list_slot)
            # adding single quotes around the string for SQL query
            list_str = "'{}'".format(list_str)
            return list_str

    def convert_duration(self, d):
        duration = 0
        if "h" in d:
            duration = int(''.join(c for c in d if c not in "hours")) * 60 
        else:
            duration = int(''.join(c for c in d if c not in "minutes"))
        return duration

    def format_date(self, D):
        date = D[0:2] + "/" + D[3:5] + "/" + D[6:10]
        return date

    def get_session(self):
        return self.session
