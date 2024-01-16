import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
import random
import requests
from time import sleep
from dad_joke.rules import DadJoke


class Kowalski():
    """Class to instantiate Kowalski."""

    def __init__(self, name=None):
        if name is None:
            self.name = 'Skipper'
        else:
            self.name = name
        self.name = self.name
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.say('I am Kowalski')

        self.joke = DadJoke()

        sleep(0.5)
        self.engine.say(self._get_greeting_(self.name))
        self.engine.runAndWait()

    def speak_va(self, response):
        """
        Speak the input string.
        """
        self.engine.say(response)
        self.engine.runAndWait()

    def input_query(self, query):
        """Enter a typed query"""
        self.activate_va(query)

    def activate_va(self, query):
        user_query = query
        print('user query ....', user_query)

        if 'time' in user_query:
            current_time = self._current_time_()
            print(f"the current time is {current_time}")
            self.speak_va(f"the current time is {current_time}")

        elif 'open website' in user_query:
            self.speak_va(
                "Please type the name of the website that you want to open (specify the full url) \n")
            website_name = input()
            print(website_name)
            webbrowser.get(
                'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(website_name)
            self.speak_va(f"{website_name} opened.")

        elif 'wikipedia' in user_query:
            self.speak_va("Searching on Wikipedia")
            user_query = user_query.replace('wikipedia ', '')
            result = wikipedia.summary(user_query, sentences=2, auto_suggest=False)
            print(result)
            self.speak_va(result)

        elif 'status report' in user_query:
            # sr = random.choice(["our supply of cheesy dibbles is running dangerously low",
            #                     'ten seconds to impact',
            #                     'the muffin will detonate in t minus two minutes',
            #                     'five percent chance of glory and Adventure'])
            sr = random.choice(['96 percent chance of deliciousness',
                                '57 percent of perfect muffins'
                                ''])
            self.speak_va(sr)

        elif 'joke' in user_query:

            if 'hear' in user_query:
                init = random.choice(['Sure, lets hear it', 'Ok, as long as its not a dad joke'])
                self.speak_va(init)
                sleep(1)
                self.speak_va("Whats the setup? (please type) ")
                setup = input()
                sleep(1)
                self.speak_va("Hmmmmmmm. I'm not sure. Whats the punchline? (please type) ")
                punchline = input()
                self.joke._learn_joke_(setup=setup, punchline=punchline)
                self.speak_va(self.joke._get_response_())

            else:
                setup, punchline = self.joke.get_joke()
                init = random.choice(['Here is one', 'Ive got one for you', 'Hey {}'.format(self.name), 'Heres a joke'])
                self.speak_va(init)
                sleep(0.2)
                self.speak_va(setup)
                sleep(1)
                self.speak_va(punchline)
                sleep(0.1)

        elif 'search' in user_query:
            self.speak_va("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get(
                'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
            self.speak_va(f"here are the results for the search term: {search_term}")

    @staticmethod
    def _current_time_():
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        return current_time

    @staticmethod
    def _get_greeting_(name):
        """
        Randomly select a greeting.
        """
        greetings = ['What can I do for you?',
                     'Would you like a cheesy dibble?',
                     'Whats the plan {}?'.format(name)]
        return random.choice(greetings)