# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="interview_bot"
)

mycursor = mydb.cursor()

tmp_question_id   = ""
tmp_program_type   = ""
tmp_answer_option = ""
count = 1
inner_count = 1

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World!")

        return []

class ActionProgramSkills(Action):

    

    def name(self) -> Text:
        return "action_program_skills"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        global cursor, count, inner_count, tmp_question_id, tmp_program_type
        
        program_type = tracker.get_slot("program_type")

        N = len(program_type)

        if N > 1:
            dispatcher.utter_message("Please tell me any one programming skill. we will start Test")

        else:
            program = program_type[0]
            dispatcher.utter_message(f"Hello Welcome To Our {program} Programming World!")

            if program == "r":

                pr = program[:2]

                if inner_count > 2:
                    inner_count = 1

                if 3 > count > 0:
                    question_id = f"{pr}_easy_{inner_count}"
                    inner_count = inner_count + 1

                elif 5 > count > 2:
                    question_id = f"{pr}_medium_{inner_count}"
                    inner_count = inner_count + 1
                
                elif 7 > count > 4:
                    question_id = f"{pr}_hard_{inner_count}"
                    inner_count = inner_count + 1
                
                else:
                    dispatcher.utter_message(f"your {program} program test completed. are you interested to see your result?")
                    return [SlotSet('result_type',False), SlotSet('program_type',program_type)]

                print("program", program, "question_id", question_id)

                sql = """
                SELECT question FROM program_question_answer WHERE question_id = %s
                """
                
                mycursor.execute(sql, (question_id, ))

                myresult = mycursor.fetchall()

                for x in myresult:
                    dispatcher.utter_message(x[0])
                
                count = count + 1

                tmp_question_id = question_id

                tmp_program_type = program
                

        return [SlotSet('result_type',True), SlotSet('program_type',program_type)]

class ActionProgramResultChecker(Action):

    global cursor

    def name(self) -> Text:
        return "action_program_result_checker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global tmp_question_id, tmp_program_type
        
        program_type = tracker.get_slot("program_type")
        option_type = tracker.get_slot("option_type")

        N = len(option_type)
        M = len(program_type)

        if N > 1 and M > 1:
            dispatcher.utter_message("choose any one langauge and answer option.:)")
        elif N > 1:
            dispatcher.utter_message("choose any one answer option.:)")
        else:
            program = program_type[0]
            if program == tmp_program_type:

                question_id = tmp_question_id

                print("program", program, "question_id", question_id, "option_type", option_type)
                
                sql = """
                SELECT answer FROM program_question_answer WHERE question_id = %s
                """
                mycursor.execute(sql, (question_id, ))

                myresult = mycursor.fetchall()

                for x in myresult:
                    if option_type[0].lower() == x[0]:
                        print("option result", x[0])
                        dispatcher.utter_message("your answer is correct. we will go for next question")
                    else:
                        dispatcher.utter_message("your answer is wrong. we will go for next question")
        
        return [SlotSet('result_type',True), SlotSet('program_type',program_type)]
