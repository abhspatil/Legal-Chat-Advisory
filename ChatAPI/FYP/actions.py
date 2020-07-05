# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

realdata = [['Hinduism protest', 'Propagating in Christianity', 'People are protesting for Hinduism', 'Roaming around and protesting', 'Propagation without proselytization', 'Hindu', 'Musilm', 'Christian', 'Propagate religion', 'Illegal propagation', 'Forceful change in religion'], ['Right to property', 'Confiscate property', 'Compensation for property', 'Person has took over my property', 'Illegal acquire of property', 'Government taken over property', 'Person has scammed with my property', 'Destruction of property', 'Forceful acquisition', 'Forcefully acquired', 'Asking for property', 'Government ordering for property'], ['Saw a child marriage', 'Child Marriage Act 2006\udcc2\udca0', 'How can I stop a child marriage?', 'Prohibition of Child Marriage', 'Marriage of a minor', 'Marriage', 'Child being forced to marry', 'Is child marriage a crime?', 'Marriage age', 'Children marring'], ['Child Labour', 'Adolescent Labour', 'Saw a child employed', 'Saw a minor employed', 'Small children working', 'Employment age', 'Children being forced to work', 'Child physical labour', 'Children being employed', 'Child employment'], ['Gender inequality', 'Women being paid less', 'Men being paid less', 'Girl child not being sent to school', 'Gender equality act', 'Women harassment', 'Women', 'Men', 'Gender', 'Partiality based on Gender']]


class ActionGetNews(Action):

	def name(self) -> Text:
	    return "action_get_news" 

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		catagary=tracker.get_slot('catagory')
		print(catagary)

		dispatcher.utter_message(text="Here is Your News -- "+str(catagary)) 

		return []

import requests 
import json
import time

class ActionGetArticleData(Action):

	def name(self) -> Text:
	    return "action_get_articleData"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		# api-endpoint 
		catagary=tracker.get_slot('catagory')
		print(catagary)
		
		endPoint="15.206.161.203"
		URL = "http://"+endPoint+":8000/getData?key="+catagary
		print(URL) 
		try:
			r = requests.get(url = URL)
			data = r.json() 
			#data="aaaaa" 
			#dispatcher.utter_message(text="Here is Your Data -- "+str(data)) 
			dispatcher.utter_message(str(data)) 
		
		except:
			dispatcher.utter_message(text="Server Not Running Please Try Again..")
			
		return []
