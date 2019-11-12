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
* inform
    - utter_ask_skills
* inform{"program_type": "Python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "Python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* deny
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "Java"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "JAVA"}
    - action_program_skills

## interactive_story_1
* mood_great
* inform
* inform
    - utter_ask_skills
* inform{"program_type": "C++"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "c"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - action_python_program
* inform{"program_type": "c"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - action_python_program
* inform{"program_type": "c"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program
* inform{"program_type": "java"}
    - slot{"program_type": "java"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program
* inform{"program_type": "c"}
    - slot{"program_type": "c"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": "python"}
    - action_python_program
* inform{"program_type": "JAVA"}
    - slot{"program_type": "JAVA"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_did_that_help
* inform
    - utter_ask_skills
* inform{"program_type": "r"}
    - slot{"program_type": "r"}
    - action_program_skills
* inform{"program_type": "c"}
    - slot{"program_type": "c"}
    - action_program_skills

## interactive_story_1
* greet
    - utter_greet
