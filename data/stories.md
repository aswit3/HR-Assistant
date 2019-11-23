## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* greet
    - action_hello_world

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "R"}
    - slot{"program_type": ["c", "c++", "java", "python", "R"]}
    - action_program_skills

## interactive_story_1
* inform{"program_type": "JAVA"}
    - slot{"program_type": ["JAVA"]}
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": ["python"]}
    - action_program_skills
