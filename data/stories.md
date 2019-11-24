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

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"program_type": ["r"]}
* inform{"program_type": "java"}
    - slot{"program_type": ["java"]}
* inform{"program_type": "java"}
    - slot{"program_type": ["java"]}
    - action_program_skills
    - slot{"program_type": ["java"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"program_type": ["r"]}

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* inform
    - utter_ask_skills
* inform{"program_type": "python"}
    - slot{"program_type": ["c", "python"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["c", "python"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
* inform{"program_type": "java"}
    - slot{"program_type": ["java"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["java"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "A"}
    - slot{"option_type": ["A"]}
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_skills
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "A"}
    - slot{"option_type": ["A"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "b"}
    - slot{"option_type": ["b"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "A"}
    - slot{"option_type": ["A"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "B"}
    - slot{"option_type": ["B"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* inform{"program_type": "r"}
    - slot{"program_type": ["r"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "A"}
    - slot{"option_type": ["A"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "B"}
    - slot{"option_type": ["B"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "C"}
    - slot{"option_type": ["C"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "C"}
    - slot{"option_type": ["C"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "c"}
    - slot{"option_type": ["c"]}
    - action_program_skills
    - slot{"result_type": true}
    - slot{"program_type": ["r"]}
* answer{"option_type": "c"}
    - slot{"option_type": ["c"]}
    - action_program_skills
    - slot{"result_type": false}
    - slot{"program_type": ["r"]}
* affirm
