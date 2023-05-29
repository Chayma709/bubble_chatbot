# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,



            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # service = tracker.get_slot('service')
        # p_count = tracker.get_slot('p_count')
        # print(service, p_count)
        # dispatcher.utter_message(text="Hi there, you booked {p_count} {service} tickets.")
        dispatcher.utter_message(text="Hello Chichooo !")

        return []