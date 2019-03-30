from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction, EntityFormField
from rasa_core.slots import DataSlot
from rasa_core.events import SlotSet, ReminderScheduled
from rasa_core.channels import UserMessage
from rasa_core.dispatcher import Button

from sql_api import SQL_API
import chart
from user import User, Crisis

from datetime import datetime as date
from datetime import timedelta
import time

api = SQL_API()

class ActionUser(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("name", "name"),
            EntityFormField("age", "age"),
            EntityFormField("gender", "gender")
        ]

    def name(self):
        return 'action_add_user'

    def submit(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        user = api.get_user(sender_id)

        if user is None:
            name = tracker.get_slot("name")
            age = tracker.get_slot("age")
            gender = tracker.get_slot("gender")
            api.insert_user(sender_id, name, age, gender)
            return [SlotSet("user_id", sender_id), 
                    SlotSet("name", name), 
                    SlotSet("age", age), 
                    SlotSet("gender", gender)]
        
class ActionCrisis(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("date", "date"),
            EntityFormField("time", "time"),
            EntityFormField("duration", "duration"),
            EntityFormField("location", "location"),
            EntityFormField("is_alone", "is_alone")
        ]

    def name(self):
        return 'action_add_crisis'

    def submit(self, dispatcher, tracker, domain):
        D = tracker.get_slot("date")
        d = tracker.get_slot("duration")
        time = tracker.get_slot("time")
        location = tracker.get_slot("location")
        is_alone = tracker.get_slot("is_alone")
        food_list = tracker.get_slot("food")

        # format date DD/MM/YY  
        date = api.format_date(D)
        # check if duration is in hour(s) => convert to minutes
        duration = api.convert_duration(d)

        food_str = api.list_to_str(food_list)
        sender_id = api.get_session().get_sender_id()
        crisis = api.insert_crisis(sender_id, date, time, duration, location, is_alone, food_str)
        crisisID = crisis.get_id()
        try: 
            api.update_profile(sender_id, crisisID)
        except:
            # if bot asked about the crisis before asking about your profile
            return None

class ActionBefore(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        return [
            EntityFormField("activity", "activity_before"),
            EntityFormField("mood", "mood_before"),
            EntityFormField("thoughts", "thoughts_before"),
        ]

    def name(self):
        return 'action_before'

    def submit(self, dispatcher, tracker, domain):
        activity = tracker.get_slot("activity_before")
        mood = tracker.get_slot("mood_before")
        thoughts = tracker.get_slot("thoughts_before")
        sender_id = api.get_session().get_sender_id()
        api.insert_profile(sender_id, "B", activity, mood, thoughts)

class ActionAfter(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        return [
            EntityFormField("activity", "activity_after"),
            EntityFormField("mood", "mood_after"),
            EntityFormField("thoughts", "thoughts_after"),
        ]

    def name(self):
        return 'action_after'

    def submit(self, dispatcher, tracker, domain):
        activity = tracker.get_slot("activity_after")
        mood = tracker.get_slot("mood_after")
        thoughts = tracker.get_slot("thoughts_after")
        sender_id = api.get_session().get_sender_id()
        api.insert_profile(sender_id, "A", activity, mood, thoughts)
        try: 
            # get last inserted crisis
            crisis = api.get_crisis(sender_id)[-1]
            crisisID = crisis.get_id()
            api.update_profile(sender_id, crisisID)
        except:
            return None
        return [SlotSet("activity_before", None), 
                SlotSet("mood_before", None), 
                SlotSet("thoughts_before", None), 
                SlotSet("activity_after", None),
                SlotSet("mood_after", None),
                SlotSet("thoughts_after", None),
                SlotSet("date", None),
                SlotSet("time", None),
                SlotSet("duration", None),
                SlotSet("location", None),
                SlotSet("is_alone", None),
                SlotSet("food", None)]

class ActionAddCard(Action):
    def name(self):
        return "action_add_card"

    def run(self, dispatcher, tracker, domain):
        activity = tracker.get_slot("emcard")
        sender_id = api.get_session().get_sender_id()
        name = api.get_user(sender_id).get_name()
        card = api.insert_emcard(sender_id, activity)
        # if date is None then ask to set crisis
        dispatcher.utter_message("The card *" + str(card) + "* has been registered successfully.")
        dispatcher.utter_message("Let me know if you need anything else, " + name )

class ActionGetCard(Action):
    def name(self):
        return "action_get_cards"

    def run(self, dispatcher, tracker, domain):
        # emcards contains a list of Emcards objects from the current user
        sender_id = api.get_session().get_sender_id()
        emcards = api.get_emcards(sender_id)
        # check if list empty
        if not emcards:
            dispatcher.utter_message("Sorry, but you don't have any emergency cards yet! Try creating new ones.")
        else:
            dispatcher.utter_message("Your emergency cards are:\n")
            count = 1
            for card in emcards:
                dispatcher.utter_message("*Emergency card #" + str(count) + "*\n*" + str(card) + "*\n")
                count += 1
                
class ActionGetCrisis(Action):
    def name(self):
        return "action_get_crisis"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        crisis = api.get_crisis(sender_id)
        d = tracker.get_slot("date")

        # check if date is filled...
        if d is not None:
            date = api.format_date(d)
            cList = []
            for c in crisis:
                if c.get_date() == date:
                    cList.append(c)
            crisis = cList
       
        # check if list is empty
        if not crisis:
            dispatcher.utter_message("Sorry, but you don't have any episodes yet. You can always inform me about new ones.")
        else:
            dispatcher.utter_message("Here's what I found:\n")
            count = 1
            for c in crisis:
                # get profile before, profile after
                CID = c.get_id()
                profiles = api.fill_profiles(CID)
                profile_before = profiles['BEFORE']
                profile_after = profiles['AFTER']
                message = "        EPISODE #" + str(count) + "\n"
                message += "*A-  TRIGGERS*\n"
                message += str(profile_before)
                message += "*B-  BEHAVIOUR*\n"
                message += str(c)
                message += "*C-  CONSEQUENCES*\n" 
                message += str(profile_after)
                dispatcher.utter_message(message)
                count += 1
        # reset slot date 
        return [SlotSet("date", None)]

class ActionCreateCard(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("activity", "card_activity"),
            EntityFormField("time", "card_time"),
            EntityFormField("duration", "card_duration")
        ]

    def name(self):
        return 'action_create_card'

    def submit(self, dispatcher, tracker, domain):
        activity = tracker.get_slot("card_activity")
        time = tracker.get_slot("card_time")
        d = tracker.get_slot("card_duration")
        duration = api.convert_duration(d)
        sender_id = api.get_session().get_sender_id()
        card = api.insert_emcard(sender_id, activity, time, duration)
        dispatcher.utter_message("The card *" + str(card) + "* has been registered successfully.")
        return [SlotSet("time", None),
                SlotSet("duration", None)]

class ActionVerifyUser(Action):
    def name(self):
        return "action_verify_user"

    def run(self, dispatcher, tracker, domain):
        # reset tracker to original state and reset all slots
        tracker._reset()
        tracker._reset_slots()

        sender_id = api.get_session().get_sender_id()
        user = api.get_user(sender_id)
        
        if user is not None:
            name = user.get_name()
            age = user.get_age()
            gender = user.get_gender()
            dispatcher.utter_message("Welcome back!")
            return [SlotSet("user_id", sender_id), 
                    SlotSet("name", name), 
                    SlotSet("age", age), 
                    SlotSet("gender", gender)]

class ActionGetLastCrisis(Action):
    def name(self):
        return "action_get_last_crisis"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        crisis = api.get_crisis(sender_id)
        if not crisis:
            dispatcher.utter_message("Sorry, but you don't have any episodes yet. You can always inform me about new ones.")
            return None
        d = {}
        # filling dictionary with:
        # key   ->  ID of crisis
        # value ->  crisis object
        for c in crisis:
            d[c.get_id()] = c

        # getting max ID (lastest crisis)
        m = max(d.keys())
        last_crisis = d[m]
        # getting info
        date = last_crisis.get_date()
        time = last_crisis.get_time()
        duration = last_crisis.get_duration()
        location = last_crisis.get_location()
        # food as list
        food = last_crisis.get_food()
        alone = last_crisis.is_alone()

        message = "Your last episode happened on " + date + ", at " + time + ". It lasted " + str(duration) + " minutes.\n"
        message += "It occured at " + location + ".\n"
        if alone is True:
            message += "You were alone.\n"
        else:
            message += "You were not alone.\n"
        message += "You had:\n"
        for f in food:
            message += "\t- " + f + "\n"

        dispatcher.utter_message(message)

class ActionPickCard(Action):
    def name(self):
        return "action_pick_card"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        cards = api.get_emcards(sender_id)
        if cards is None:
            dispatcher.utter_message("You don't have emergency cards to use. Try creating one!")
        else:
            buttons = []
            for card in cards:
                activity = card.get_activity()
                id = card.get_id()
                button = Button(title = activity, payload = "/pick_card{\"emcard\":\"" + activity + "\",\"card_id\":\"" + str(id) + "\"}")
                buttons.append(button)
                
            dispatcher.utter_button_message("Pick an emergency card and use it.", buttons)
            return [ReminderScheduled("action_reminder_cards", date.now() + timedelta(seconds=15))]

class ActionHelpWithCards(Action):
    def name(self):
        return "action_help_with_cards"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        crisis = api.get_crisis(sender_id)

        if crisis is None:
            dispatcher.utter_message("Sorry, but I can't help you if you don't inform me about your episodes!")
        else:
            for c in crisis:
                # each crisis has 2 profiles
                profiles = api.get_profiles(c.get_id())
                for p in profiles:
                    activity = p.get_activity()
                    time = c.get_time()
                    duration = c.get_duration()
                    api.insert_emcard(sender_id, activity, time, duration)
            dispatcher.utter_message("I've added some emergency cards that you can use. Check them out:")

class ActionDrawCharts(Action):
    def name(self):
        return "action_draw_charts"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        crisis = api.get_crisis(sender_id)

        if crisis is None:
            dispatcher.utter_message("Sorry, but you don't any episodes yet!")
        else:
            name = tracker.get_slot("name")
            title = name + "'s statistics"
            filename = 'chart_' + str(sender_id)
            url = chart.draw_chart(api, crisis, title, filename)
            dispatcher.utter_message("Take a look at your statistics:")
            dispatcher.utter_attachment(url)

class ActionShowProgress(Action):
    def name(self):
        return "action_show_progress"

    def run(self, dispatcher, tracker, domain):
        sender_id = api.get_session().get_sender_id()
        crisis = api.get_crisis(sender_id)
        d = {}
        for c in crisis:
            d[c.get_id()] = c.get_duration()
        k1 = max(d.keys())
        v1 = d.pop(k1)
        k2 = max(d.keys())
        v2 = d.pop(k2)
        if (v1 < v2):
            dispatcher.utter_message("*You are making progress!*")
            dispatcher.utter_message("Last time, your episode lasted " + str(v1) + " minutes , which is " + str(v2-v1) + " minutes less than the previous one! Keep up the good work!")
        d = {}
        for c in crisis:
            d[c.get_id()] = c.get_food()
        k1 = max(d.keys())
        f1 = d.pop(k1)
        k2 = max(d.keys())
        f2 = d.pop(k2)
        l1 = len(f1)
        l2 = len(f2)
        if (l1 < l2):
            if (v1 > v2):
                dispatcher.utter_message("*You are making progress!*")
            dispatcher.utter_message("Last time, you had less food than before!")
        dispatcher.utter_message("Let me give you some tips:")

# reminder classes
class ActionReminderHelp(Action):
    def name(self):
        return "action_reminder_help"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_reminder_help", tracker)

class ActionReminderCards(Action):
    def name(self):
        return "action_reminder_cards"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_reminder_cards", tracker)

class ActionAskHelpful(Action):
    def name(self):
        return "action_ask_helpful"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_ask_helpful", tracker)
        return [ReminderScheduled("action_reminder_help", date.now() + timedelta(seconds=15))]

# same function as the above but different name (for the stories)
class ActionAskHelpfulCards(Action):
    def name(self):
        return "action_ask_helpful_card"

    def run(self, dispatcher, tracker, domain):
        #sender_id = api.get_session().get_sender_id()
        #name = api.get_user(sender_id).get_name()
        # SlotSet("name", name)
        dispatcher.utter_template("utter_ask_helpful", tracker)
        return [ReminderScheduled("action_ask_helpful_card", date.now() + timedelta(seconds=15))]