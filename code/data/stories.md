######################################
# reminder 1
    - action_reminder_help
    - action_ask_helpful
* helpful
    - utter_ask_next_action

    - action_reminder_help
    - action_ask_helpful
* not_helpful
    - utter_cheer_up
    - action_ask_helpful

# reminder pick card helpful
    - action_reminder_cards
    - action_pick_card
* pick_card
    - utter_selected_card
    - action_ask_helpful_card
* helpful
    - utter_glad

# reminder pick card not helpful (recursive)
    - action_reminder_cards
    - action_pick_card
* pick_card
    - utter_selected_card
    - action_ask_helpful_card
* not_helpful
    - utter_sorry
    - action_pick_card

#####################################
## story start
* start
    - utter_greet

## story greet
* greet
    - action_verify_user
    - action_add_user

## story goodbye
* goodbye
    - utter_goodbye

## story inform crisis before
* inform
    - utter_sorry
    - action_before

## story get crisis
* ask_crisis
    - action_get_crisis

# story ask last crisis
* ask_last_crisis
    - action_get_last_crisis

## story get cards
* ask_cards
    - action_get_cards

## story create new card
* create_card
    - action_create_card
* inform
    - action_create_card
* inform
    - action_create_card
    - action_create_card

# story suggest more cards
* ask_suggestions
    - utter_suggest_cards
* inform
    - action_add_card

## story ask help 1
* ask_help
    - utter_take_it_easy
    - utter_ask_current_location
* inform
    - utter_get_out
    - action_ask_helpful
* helpful
    - utter_ask_next_action

## story ask help 2
* ask_help
    - utter_take_it_easy
    - utter_ask_current_location
* inform
    - utter_get_out
    - action_ask_helpful
* not_helpful
    - utter_cheer_up
    - action_ask_helpful
* not_helpful
    - utter_sorry
    
## story ask help 3
* ask_help
    - utter_take_it_easy
    - utter_ask_current_location
* inform
    - utter_get_out
    - action_ask_helpful
* not_helpful
    - utter_cheer_up
    - action_ask_helpful
* helpful
    - utter_ask_next_action

## Ask next action
# story pick a card helpful
* pick_card
    - action_pick_card
* pick_card
    - utter_selected_card
    - action_ask_helpful_card
* helpful
    - utter_glad

# story pick a card not helpful (recurvise)
* pick_card
    - action_pick_card
* pick_card
    - utter_selected_card
    - action_ask_helpful_card
* not_helpful
    - utter_sorry
    - action_pick_card

# story prevent crisis
* need_help
    - action_help_with_cards
    - action_pick_card

# story ask statistics
* ask_stats
    - action_draw_charts

# story give up
* give_up
    - action_show_progress
    - utter_tips
    - utter_fun_facts

# story ask tips
* ask_tips
    - utter_tips
    - utter_fun_facts

## Generated Story -6809437767845252832
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "paul"}
    - slot{"name": "paul"}
    - action_add_user
    - slot{"name": "paul"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "18"}
    - slot{"age": "18"}
    - action_add_user
    - slot{"age": "18"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 1}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "watching a movie"}
    - action_before
    - slot{"activity_before": "watching a movie"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "excited"}
    - action_before
    - slot{"mood_before": "excited"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "movies"}
    - action_before
    - slot{"thoughts_before": "movies"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "06.08.2018"}
    - slot{"date": "06.08.2018"}
    - action_add_crisis
    - slot{"date": "06.08.2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "09:15"}
    - slot{"time": "09:15"}
    - action_add_crisis
    - slot{"time": "09:15"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "20 min"}
    - slot{"duration": "20 min"}
    - action_add_crisis
    - slot{"duration": "20 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "home"}
    - slot{"location": "home"}
    - action_add_crisis
    - slot{"location": "home"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "1"}
    - slot{"is_alone": "1"}
    - utter_ask_food
* inform{"food": "pancakes"}
    - slot{"food": ["burger", "pancakes"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "running"}
    - action_after
    - slot{"activity_after": "running"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "stressed"}
    - action_after
    - slot{"mood_after": "stressed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "work"}
    - action_after
    - slot{"thoughts_after": "work"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "go to a concert"}
    - slot{"emcard": "go to a concert"}
    - action_add_card
    - slot{"emcard": "go to a concert"}
* goodbye
    - utter_goodbye
    - action_restart
    - export

## Generated Story 3734322589144896068
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "paul"}
    - slot{"age": 18}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
    - export

## Generated Story -5596206413190187298
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "paul"}
    - slot{"age": 18}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_crisis{"date": "06.08.2018"}
    - slot{"date": "06.08.2018"}
    - action_get_crisis
    - slot{"date": null}
    - export

## Generated Story -7738377174571789603
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "paul"}
    - slot{"age": 18}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* create_card
    - action_create_card
    - slot{"requested_slot": "card_activity"}
* inform{"activity": "playing video games"}
    - action_create_card
    - slot{"card_activity": "playing video games"}
    - slot{"requested_slot": "card_time"}
* inform{"time": "11:00"}
    - slot{"time": "11:00"}
    - action_create_card
    - slot{"card_time": "11:00"}
    - slot{"requested_slot": "card_duration"}
* inform{"duration": "1 hour"}
    - slot{"duration": "1 hour"}
    - action_create_card
    - slot{"card_duration": "1 hour"}
    - export

## Generated Story 3741851044142012741
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "paul"}
    - slot{"age": 18}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_cards
    - action_get_cards
    - export

## Generated Story 8037216595690954541
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "anna"}
    - slot{"name": "anna"}
    - action_add_user
    - slot{"name": "anna"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "23"}
    - slot{"age": "23"}
    - action_add_user
    - slot{"age": "23"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "female"}
    - slot{"gender": "female"}
    - action_add_user
    - slot{"gender": "female"}
    - slot{"user_id": 2}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "listening to music"}
    - action_before
    - slot{"activity_before": "listening to music"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "sad"}
    - action_before
    - slot{"mood_before": "sad"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "school"}
    - action_before
    - slot{"thoughts_before": "school"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "03-13-2017"}
    - slot{"date": "03-13-2017"}
    - action_add_crisis
    - slot{"date": "03-13-2017"}
    - slot{"requested_slot": "time"}
* inform{"time": "15:45"}
    - slot{"time": "15:45"}
    - action_add_crisis
    - slot{"time": "15:45"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "2 hrs"}
    - slot{"duration": "2 hrs"}
    - action_add_crisis
    - slot{"duration": "2 hrs"}
    - slot{"requested_slot": "location"}
* inform{"location": "work"}
    - slot{"location": "work"}
    - action_add_crisis
    - slot{"location": "work"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "donuts"}
    - slot{"food": ["pizza", "donuts"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "sleeping"}
    - action_after
    - slot{"activity_after": "sleeping"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "relaxed"}
    - action_after
    - slot{"mood_after": "relaxed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "nature"}
    - action_after
    - slot{"thoughts_after": "nature"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "call a friend"}
    - slot{"emcard": "call a friend"}
    - action_add_card
    - slot{"emcard": "call a friend"}
* goodbye
    - utter_goodbye
    - export

## Generated Story -1637056125883086479
* greet
    - action_verify_user
    - slot{"user_id": 2}
    - slot{"name": "anna"}
    - slot{"age": 23}
    - slot{"gender": "F"}
    - action_add_user
    - utter_ask_help
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* ask_cards
    - action_get_cards
    - export

## Generated Story -2274077594798605451
* greet
    - action_verify_user
    - slot{"user_id": 2}
    - slot{"name": "michel"}
    - slot{"age": 20}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_cards
    - action_get_cards
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
    - export

## Generated Story 7004877207821371686
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "melissa"}
    - slot{"name": "melissa"}
    - action_add_user
    - slot{"name": "melissa"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "25"}
    - slot{"age": "25"}
    - action_add_user
    - slot{"age": "25"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "female"}
    - slot{"gender": "female"}
    - action_add_user
    - slot{"gender": "female"}
    - slot{"user_id": 1}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "playing on the phone"}
    - action_before
    - slot{"activity_before": "playing on the phone"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "bored"}
    - action_before
    - slot{"mood_before": "bored"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "girlfriend"}
    - action_before
    - slot{"thoughts_before": "girlfriend"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "06.08.2018"}
    - slot{"date": "06.08.2018"}
    - action_add_crisis
    - slot{"date": "06.08.2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "13:50"}
    - slot{"time": "13:50"}
    - action_add_crisis
    - slot{"time": "13:50"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "23 min"}
    - slot{"duration": "23 min"}
    - action_add_crisis
    - slot{"duration": "23 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "mall"}
    - slot{"location": "mall"}
    - action_add_crisis
    - slot{"location": "mall"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "1"}
    - slot{"is_alone": "1"}
    - utter_ask_food
* inform{"food": "burger"}
    - slot{"food": ["pizza", "burger"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "studying"}
    - action_after
    - slot{"activity_after": "studying"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "happy"}
    - action_after
    - slot{"mood_after": "happy"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "exams"}
    - action_after
    - slot{"thoughts_after": "exams"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "watch a movie"}
    - slot{"emcard": "watch a movie"}
    - action_add_card
    - slot{"emcard": "watch a movie"}
* goodbye
    - utter_goodbye
    - export

## Generated Story 4339039167665055105
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "jessica"}
    - slot{"age": 19}
    - slot{"gender": "F"}
    - action_add_user
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "sleeping"}
    - action_before
    - slot{"activity_before": "sleeping"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "sad"}
    - action_before
    - slot{"mood_before": "sad"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "girlfriend"}
    - action_before
    - slot{"thoughts_before": "girlfriend"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "07.08.2018"}
    - slot{"date": "07.08.2018"}
    - action_add_crisis
    - slot{"date": "07.08.2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "13:50"}
    - slot{"time": "13:50"}
    - action_add_crisis
    - slot{"time": "13:50"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "17 min"}
    - slot{"duration": "17 min"}
    - action_add_crisis
    - slot{"duration": "17 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "home"}
    - slot{"location": "home"}
    - action_add_crisis
    - slot{"location": "home"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "fries"}
    - slot{"food": ["burger", "donuts", "fries"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "reading a book"}
    - action_after
    - slot{"activity_after": "reading a book"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "anxious"}
    - action_after
    - slot{"mood_after": "anxious"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "work"}
    - action_after
    - slot{"thoughts_after": "work"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
    - export

## Generated Story 7404276365965291648
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "adam"}
    - slot{"name": "adam"}
    - action_add_user
    - slot{"name": "adam"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "27"}
    - slot{"age": "27"}
    - action_add_user
    - slot{"age": "27"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 1}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "studying"}
    - action_before
    - slot{"activity_before": "studying"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "frustrated"}
    - action_before
    - slot{"mood_before": "frustrated"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "exams"}
    - action_before
    - slot{"thoughts_before": "exams"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "08-04-2018"}
    - slot{"date": "08-04-2018"}
    - action_add_crisis
    - slot{"date": "08-04-2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "06:30"}
    - slot{"time": "06:30"}
    - action_add_crisis
    - slot{"time": "06:30"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "18 min"}
    - slot{"duration": "18 min"}
    - action_add_crisis
    - slot{"duration": "18 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "restaurant"}
    - slot{"location": "restaurant"}
    - action_add_crisis
    - slot{"location": "restaurant"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "1"}
    - slot{"is_alone": "1"}
    - utter_ask_food
* inform{"food": "bacon"}
    - slot{"food": ["eggs", "bacon"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "reading a book"}
    - action_after
    - slot{"activity_after": "reading a book"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "lonely"}
    - action_after
    - slot{"mood_after": "lonely"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "animals"}
    - action_after
    - slot{"thoughts_after": "animals"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "take a walk"}
    - slot{"emcard": "take a walk"}
    - action_add_card
    - slot{"emcard": "take a walk"}
    - export

## Generated Story 5727558928816827641
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "adam"}
    - slot{"age": 27}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_suggestions
    - utter_suggest_cards
* inform{"emcard": "take a long shower"}
    - slot{"emcard": "take a long shower"}
    - action_add_card
    - slot{"emcard": "take a long shower"}
* ask_cards
    - action_get_cards
    - export

## Generated Story 2024790939550806810
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "jessica"}
    - slot{"name": "jessica"}
    - action_add_user
    - slot{"name": "jessica"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "17"}
    - slot{"age": "17"}
    - action_add_user
    - slot{"age": "17"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "female"}
    - slot{"gender": "female"}
    - action_add_user
    - slot{"gender": "female"}
    - slot{"user_id": 1}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "swiming"}
    - action_before
    - slot{"activity_before": "swiming"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "excited"}
    - action_before
    - slot{"mood_before": "excited"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "food"}
    - action_before
    - slot{"thoughts_before": "food"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "02-08-2018"}
    - slot{"date": "02-08-2018"}
    - action_add_crisis
    - slot{"date": "02-08-2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "14:18"}
    - slot{"time": "14:18"}
    - action_add_crisis
    - slot{"time": "14:18"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "1 hr"}
    - slot{"duration": "1 hr"}
    - action_add_crisis
    - slot{"duration": "1 hr"}
    - slot{"requested_slot": "location"}
* inform{"location": "pool"}
    - slot{"location": "pool"}
    - action_add_crisis
    - slot{"location": "pool"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "1"}
    - slot{"is_alone": "1"}
    - utter_ask_food
* inform{"food": "icecream"}
    - slot{"food": ["pancakes", "icecream"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "sleeping"}
    - action_after
    - slot{"activity_after": "sleeping"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "relaxed"}
    - action_after
    - slot{"mood_after": "relaxed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "boyfriend"}
    - action_after
    - slot{"thoughts_after": "boyfriend"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "surf the internet"}
    - slot{"emcard": "surf the internet"}
    - action_add_card
    - slot{"emcard": "surf the internet"}
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* ask_cards
    - action_get_cards
* goodbye
    - utter_goodbye
    - export

## Generated Story -3212697848709727114
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "jessica"}
    - slot{"age": 17}
    - slot{"gender": "F"}
    - action_add_user
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "eating"}
    - action_before
    - slot{"activity_before": "eating"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "happy"}
    - action_before
    - slot{"mood_before": "happy"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "work"}
    - action_before
    - slot{"thoughts_before": "work"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "07/08/2017"}
    - slot{"date": "07/08/2017"}
    - action_add_crisis
    - slot{"date": "07/08/2017"}
    - slot{"requested_slot": "time"}
* inform{"time": "22:10"}
    - slot{"time": "22:10"}
    - action_add_crisis
    - slot{"time": "22:10"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "15 min"}
    - slot{"duration": "15 min"}
    - action_add_crisis
    - slot{"duration": "15 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "beach"}
    - slot{"location": "beach"}
    - action_add_crisis
    - slot{"location": "beach"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "salad"}
    - slot{"food": ["burger"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "watching a movie"}
    - action_after
    - slot{"activity_after": "watching a movie"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "sad"}
    - action_after
    - slot{"mood_after": "sad"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "food"}
    - action_after
    - slot{"thoughts_after": "food"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "go to a concert"}
    - slot{"emcard": "go to a concert"}
    - action_add_card
    - slot{"emcard": "go to a concert"}
* ask_suggestions
    - utter_suggest_cards
* inform{"emcard": "buy someone a gift"}
    - slot{"emcard": "buy someone a gift"}
    - action_add_card
    - slot{"emcard": "buy someone a gift"}
* goodbye
    - utter_goodbye
    - export

## Generated Story -2135389346533732755
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "jessica"}
    - slot{"age": 17}
    - slot{"gender": "F"}
    - action_add_user
    - utter_ask_help
* create_card
    - action_create_card
    - slot{"requested_slot": "card_activity"}
* inform{"activity": "listening to linkin park"}
    - action_create_card
    - slot{"card_activity": "listening to linkin park"}
    - slot{"requested_slot": "card_time"}
* inform{"time": "14:00"}
    - slot{"time": "14:00"}
    - action_create_card
    - slot{"card_time": "14:00"}
    - slot{"requested_slot": "card_duration"}
* inform{"duration": "10 min"}
    - slot{"duration": "10 min"}
    - action_create_card
    - slot{"card_duration": "10 min"}
* ask_cards
    - action_get_cards
    - export

## Generated Story -7973015747560932297
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "peter"}
    - slot{"name": "peter"}
    - action_add_user
    - slot{"name": "peter"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "16"}
    - slot{"age": "16"}
    - action_add_user
    - slot{"age": "16"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 1}
    - utter_ask_help
* ask_cards
    - action_get_cards
* goodbye
    - utter_goodbye
    - export

## Generated Story -7973015747560932297
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "peter"}
    - slot{"name": "peter"}
    - action_add_user
    - slot{"name": "peter"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "16"}
    - slot{"age": "16"}
    - action_add_user
    - slot{"age": "16"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 1}
    - utter_ask_help
* ask_cards
    - action_get_cards
* goodbye
    - utter_goodbye
    - export

## Generated Story 9089515383959935494
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "melissa"}
    - slot{"name": "melissa"}
    - action_add_user
    - slot{"name": "melissa"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "26"}
    - slot{"age": "26"}
    - action_add_user
    - slot{"age": "26"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "female"}
    - slot{"gender": "female"}
    - action_add_user
    - slot{"gender": "female"}
    - slot{"user_id": 1}
    - utter_ask_help
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "listening to music"}
    - action_before
    - slot{"activity_before": "listening to music"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "worried"}
    - action_before
    - slot{"mood_before": "worried"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "school"}
    - action_before
    - slot{"thoughts_before": "school"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "28/01/2016"}
    - slot{"date": "28/01/2016"}
    - action_add_crisis
    - slot{"date": "28/01/2016"}
    - slot{"requested_slot": "time"}
* inform{"time": "12:34"}
    - slot{"time": "12:34"}
    - action_add_crisis
    - slot{"time": "12:34"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "37 min"}
    - slot{"duration": "37 min"}
    - action_add_crisis
    - slot{"duration": "37 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "park"}
    - slot{"location": "park"}
    - action_add_crisis
    - slot{"location": "park"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "salad"}
    - slot{"food": ["sandwich", "salad"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "playing video games"}
    - action_after
    - slot{"activity_after": "playing video games"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "happy"}
    - action_after
    - slot{"mood_after": "happy"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "cars"}
    - action_after
    - slot{"thoughts_after": "cars"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "call a friend"}
    - slot{"emcard": "call a friend"}
    - action_add_card
    - slot{"emcard": "call a friend"}
    - export

## Generated Story 875365585882648838
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "melissa"}
    - slot{"age": 26}
    - slot{"gender": "F"}
    - action_add_user
    - utter_ask_help
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* ask_suggestions
    - utter_suggest_cards
* inform{"emcard": "dance to a favorite song"}
    - slot{"emcard": "dance to a favorite song"}
    - action_add_card
    - slot{"emcard": "dance to a favorite song"}
* ask_cards
    - action_get_cards
* goodbye
    - utter_goodbye
    - export

## Generated Story 2950049332095231557
* greet
    - action_verify_user
    - slot{"user_id": 1}
    - slot{"name": "michel"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_last_crisis
    - action_get_last_crisis
    - slot{"date": "05/02/2015"}
    - slot{"time": "18:00"}
    - slot{"duration": 60}
    - slot{"location": "gym"}
    - slot{"food": ["burger", "fries"]}
    - export

## Generated Story -7590669675140518073
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "johnny"}
    - slot{"name": "johnny"}
    - action_add_user
    - slot{"name": "johnny"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "19"}
    - slot{"age": "19"}
    - action_add_user
    - slot{"age": "19"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 2}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "jumping"}
    - action_before
    - slot{"activity_before": "jumping"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "anxious"}
    - action_before
    - slot{"mood_before": "anxious"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "girlfriend"}
    - action_before
    - slot{"thoughts_before": "girlfriend"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "20-07-2018"}
    - slot{"date": "20-07-2018"}
    - action_add_crisis
    - slot{"date": "20-07-2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "13:00"}
    - slot{"time": "13:00"}
    - action_add_crisis
    - slot{"time": "13:00"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "10 min"}
    - slot{"duration": "10 min"}
    - action_add_crisis
    - slot{"duration": "10 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "zoo"}
    - slot{"location": "zoo"}
    - action_add_crisis
    - slot{"location": "zoo"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "donuts"}
    - slot{"food": ["pancakes", "donuts"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "walking"}
    - action_after
    - slot{"activity_after": "walking"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "annoyed"}
    - action_after
    - slot{"mood_after": "annoyed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "turtles"}
    - action_after
    - slot{"thoughts_after": "turtles"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "dance to a favorite song"}
    - slot{"emcard": "dance to a favorite song"}
    - action_add_card
    - slot{"emcard": "dance to a favorite song"}
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "reading"}
    - action_before
    - slot{"activity_before": "reading"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "hungry"}
    - action_before
    - slot{"mood_before": "hungry"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "food"}
    - action_before
    - slot{"thoughts_before": "food"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "07.06.2019"}
    - slot{"date": "07.06.2019"}
    - action_add_crisis
    - slot{"date": "07.06.2019"}
    - slot{"requested_slot": "time"}
* inform{"time": "16:17"}
    - slot{"time": "16:17"}
    - action_add_crisis
    - slot{"time": "16:17"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "2 hrs"}
    - slot{"duration": "2 hrs"}
    - action_add_crisis
    - slot{"duration": "2 hrs"}
    - slot{"requested_slot": "location"}
* inform{"location": "rooftop"}
    - slot{"location": "rooftop"}
    - action_add_crisis
    - slot{"location": "rooftop"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "pasta"}
    - slot{"food": ["beef", "pasta"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "praying"}
    - action_after
    - slot{"activity_after": "praying"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "depressed"}
    - action_after
    - slot{"mood_after": "depressed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "death"}
    - action_after
    - slot{"thoughts_after": "death"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* goodbye
    - utter_goodbye
    - export

## Generated Story -4669926826969451152
* greet
    - action_verify_user
    - action_add_user
    - slot{"requested_slot": "name"}
* personal_info{"name": "peter"}
    - slot{"name": "peter"}
    - action_add_user
    - slot{"name": "peter"}
    - slot{"requested_slot": "age"}
* personal_info{"age": "18"}
    - slot{"age": "18"}
    - action_add_user
    - slot{"age": "18"}
    - slot{"requested_slot": "gender"}
* personal_info{"gender": "male"}
    - slot{"gender": "male"}
    - action_add_user
    - slot{"gender": "male"}
    - slot{"user_id": 1}
    - utter_ask_help
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "running"}
    - action_before
    - slot{"activity_before": "running"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "tried"}
    - action_before
    - slot{"mood_before": "tried"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "food"}
    - action_before
    - slot{"thoughts_before": "food"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "09-08-2018"}
    - slot{"date": "09-08-2018"}
    - action_add_crisis
    - slot{"date": "09-08-2018"}
    - slot{"requested_slot": "time"}
* inform{"time": "05:30"}
    - slot{"time": "05:30"}
    - action_add_crisis
    - slot{"time": "05:30"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "18 min"}
    - slot{"duration": "18 min"}
    - action_add_crisis
    - slot{"duration": "18 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "home"}
    - slot{"location": "home"}
    - action_add_crisis
    - slot{"location": "home"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "1"}
    - slot{"is_alone": "1"}
    - utter_ask_food
* inform{"food": "fries"}
    - slot{"food": ["burger", "donuts", "fries"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "sleeping"}
    - action_after
    - slot{"activity_after": "sleeping"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "relaxed"}
    - action_after
    - slot{"mood_after": "relaxed"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "girlfriend"}
    - action_after
    - slot{"thoughts_after": "girlfriend"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "watch a movie"}
    - slot{"emcard": "watch a movie"}
    - action_add_card
    - slot{"emcard": "watch a movie"}
* ask_cards
    - action_get_cards
* create_card
    - action_create_card
    - slot{"requested_slot": "card_activity"}
* inform{"activity": "playing video games"}
    - action_create_card
    - slot{"card_activity": "playing video games"}
    - slot{"requested_slot": "card_time"}
* greet{"time": "18:00"}
    - slot{"time": "18:00"}
    - action_create_card
    - slot{"card_time": "18:00"}
    - slot{"requested_slot": "card_duration"}
* inform{"duration": "1 hr"}
    - slot{"duration": "1 hr"}
    - action_create_card
    - slot{"card_duration": "1 hr"}
    - slot{"time": null}
    - slot{"duration": null}
* ask_cards
    - action_get_cards
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* inform
    - utter_sorry
    - action_before
    - slot{"requested_slot": "activity_before"}
* inform{"activity": "working"}
    - action_before
    - slot{"activity_before": "working"}
    - slot{"requested_slot": "mood_before"}
* inform{"mood": "angry"}
    - action_before
    - slot{"mood_before": "angry"}
    - slot{"requested_slot": "thoughts_before"}
* inform{"thoughts": "work"}
    - action_before
    - slot{"thoughts_before": "work"}
    - action_add_crisis
    - slot{"requested_slot": "date"}
* inform{"date": "08-02-2019"}
    - slot{"date": "08-02-2019"}
    - action_add_crisis
    - slot{"date": "08-02-2019"}
    - slot{"requested_slot": "time"}
* inform{"time": "15:00"}
    - slot{"time": "15:00"}
    - action_add_crisis
    - slot{"time": "15:00"}
    - slot{"requested_slot": "duration"}
* inform{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_add_crisis
    - slot{"duration": "30 min"}
    - slot{"requested_slot": "location"}
* inform{"location": "work"}
    - slot{"location": "work"}
    - action_add_crisis
    - slot{"location": "work"}
    - slot{"requested_slot": "is_alone"}
* inform{"is_alone": "0"}
    - slot{"is_alone": "0"}
    - utter_ask_food
* inform{"food": "pancakes"}
    - slot{"food": ["icecream", "pancakes"]}
    - action_add_crisis
    - action_after
    - slot{"requested_slot": "activity_after"}
* inform{"activity": "taking a shower"}
    - action_after
    - slot{"activity_after": "taking a shower"}
    - slot{"requested_slot": "mood_after"}
* inform{"mood": "satisfied"}
    - action_after
    - slot{"mood_after": "satisfied"}
    - slot{"requested_slot": "thoughts_after"}
* inform{"thoughts": "animals"}
    - action_after
    - slot{"thoughts_after": "animals"}
    - slot{"activity_before": null}
    - slot{"mood_before": null}
    - slot{"thoughts_before": null}
    - slot{"activity_after": null}
    - slot{"mood_after": null}
    - slot{"thoughts_after": null}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"duration": null}
    - slot{"location": null}
    - slot{"is_alone": null}
    - slot{"food": null}
    - utter_suggest_cards
* inform{"emcard": "surf the internet"}
    - slot{"emcard": "surf the internet"}
    - action_add_card
    - slot{"emcard": "surf the internet"}
* ask_crisis
    - action_get_crisis
    - slot{"date": null}
* ask_last_crisis
    - action_get_last_crisis
* goodbye
    - utter_goodbye
    - export

## Generated Story -5279617151801877692
* greet
    - action_verify_user
    - slot{"user_id": 502136423}
    - slot{"name": "michel"}
    - slot{"age": 19}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_help
    - utter_take_it_easy
    - utter_ask_current_location
* inform{"location": "home"}
    - slot{"location": "home"}
    - utter_get_out
    - action_ask_helpful
    - slot{"location": null}
* helpful
    - utter_ask_next_action
* ask_stats
    - action_draw_charts
* goodbye
    - utter_goodbye
    - export

## Generated Story 4386444161912083717
* greet
    - action_verify_user
    - slot{"user_id": 502136423}
    - slot{"name": "michel"}
    - slot{"age": 19}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* give_up
    - action_show_progress
    - utter_tips
    - utter_fun_facts
    - export

## Generated Story -4908777544358618050
* greet
    - action_verify_user
    - slot{"user_id": 552993321}
    - slot{"name": "zahi"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_stats
    - action_draw_charts
    - export

######################################################################
## Generated Story 8037609773784435626
* greet
    - action_verify_user
    - slot{"user_id": 552993321}
    - slot{"name": "zahi"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_help
    - utter_take_it_easy
    - utter_ask_current_location
* inform{"location": "university"}
    - slot{"location": "university"}
    - utter_get_out
    - action_ask_helpful
* helpful
    - utter_ask_next_action
* ask_stats
    - action_draw_charts
    - export

## Generated Story -3913162167536434571
* greet
    - action_verify_user
    - slot{"user_id": 552993321}
    - slot{"name": "zahi"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* pick_card
    - action_pick_card
    - export

## Generated Story -2144354662912291894
* greet
    - action_verify_user
    - slot{"user_id": 552993321}
    - slot{"name": "zahi"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* pick_card
    - action_pick_card
* pick_card{"emcard": "go hiking", "card_id": "34"}
    - slot{"card_id": "34"}
    - slot{"emcard": "go hiking"}
    - utter_selected_card
    - action_ask_helpful_card
* helpful
    - utter_glad
    - export

## Generated Story 1922587369553559047
* greet
    - action_verify_user
    - slot{"user_id": 552993321}
    - slot{"name": "zahi"}
    - slot{"age": 22}
    - slot{"gender": "M"}
    - action_add_user
    - utter_ask_help
* ask_suggestions
    - utter_suggest_cards
* inform{"emcard": "call a friend"}
    - slot{"emcard": "call a friend"}
    - action_add_card
* ask_cards
    - action_get_cards
* pick_card
    - action_pick_card
* pick_card{"emcard": "go hiking", "card_id": "34"}
    - slot{"card_id": "34"}
    - slot{"emcard": "go hiking"}
    - utter_selected_card
    - action_ask_helpful_card
* not_helpful
    - utter_sorry
    - action_pick_card
* pick_card{"emcard": "call a friend", "card_id": "35"}
    - slot{"card_id": "35"}
    - slot{"emcard": "call a friend"}
    - utter_selected_card
    - action_ask_helpful_card
* not_helpful
    - utter_sorry
    - action_pick_card
    - export











