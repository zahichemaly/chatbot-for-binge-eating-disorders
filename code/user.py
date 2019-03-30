class User:
    __userCount = 0

    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.crisis = []
        self.emcards = []
        User.__userCount += 1

    def get_name(self):
       return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def add_crisis(self, crisis):
        self.crisis.append(crisis)

    def get_crisis(self):
        return self.crisis

    def get_user_count(self):
        return User.__userCount

    def add_emcard(self, emcard):
        self.emcards.append(emcard)

    def get_emcards(self):
        return self.emcards

class Crisis:
    def __init__(self, id, date, time, duration, location, alone, food = [], profiles = {}):
        self.id = id
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.food = food
        self.alone = alone
        self.profiles = {}

    def __str__(self):
        message = "Episode on " + self.date + ", at " + self.time + ", lasted " + str(self.duration) + " minutes.\n"
        message += "It occured at " + self.location + ".\n"
        if self.alone is True:
            message += "You were alone.\n"
        else:
            message += "You were not alone.\n"
        message += "You had:\n"
        for f in self.food:
            message += "\t- " + f + "\n"
        return message

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_duration(self):
        return self.duration

    def get_location(self):
        return self.location

    def get_food(self):
        return self.food

    def is_alone(self):
        if self.alone is 0:
            return False
        else:
            return True

    def set_profile(self, context, p):
        self.profiles[context] = p

    def get_profile(self, context):
        return self.profiles[context]

class Profile:
    def __init__(self, id, context, activity, mood, thoughts):
        self.id = id
        self.context = context
        self.activity = activity
        self.mood = mood
        self.thoughts = thoughts

    def __str__(self):
        message = "You were: " + self.activity + "\n"
        message += "Your mood was: " + self.mood + "\n"
        message += "You were thinking about: " + self.thoughts + "\n"
        return message

    def get_context(self):
        return self.context

    def get_id(self):
        return self.id

    def get_activity(self):
        return self.activity

    def get_mood(self):
        return self.mood

    def get_thoughts(self):
        return self.thoughts

class Emcard:
    def __init__(self, id, activity, time, duration):
        self.id = id
        self.activity = activity
        self.time = time
        self.duration = duration

    def __str__(self):
        message = self.activity + ", at " + self.time + ", for " + str(self.duration) + " min."
        return message

    def get_id(self):
        return self.id
    
    def get_activity(self):
        return self.activity

    def get_time(self):
        return self.time

    def get_duration(self):
        return self.duration

    def set_time(self, time):
        self.time = time

    def set_duration(self, duration):
        self.duration = duration


    