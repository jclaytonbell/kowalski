"""
Python module to tell dad jokes.
"""
import csv
import random
import pandas as pd
from time import sleep

FILEPATH = r'dad_joke/jokes.csv'
IDX = 'IDX'
SETUP = 'SETUP'
PUNCHLINE = 'PUNCHLINE'

class DadJoke():
    """
    Class to define a dad joke.
    """

    def __init__(self):
        self.joke_file = FILEPATH
        self.joke_df = None
        self._load_jokes_()
        self.idx = None
        self.used = []
        self.setup = None
        self.punchline = None
        self.pause = 3

    def tell_joke(self):
        """
        Tell a dad joke!
        """
        self._get_random_joke_()
        print(self.setup)
        sleep(self.pause)
        print(' ... {}'.format(self.punchline))
        print(' ')
        sleep(1)

    def get_joke(self):
        """
        Return a dad joke!
        """
        self._get_random_joke_()
        return self.setup, self.punchline

    def learn_joke(self, setup, punchline):
        """
        Write new dad joke to joke file.
        """
        self._learn_joke_(setup, punchline)
        sleep(1)
        print(self._get_response_())

    def _learn_joke_(self, setup, punchline):
        """
        Write new dad joke to joke file.
        """
        new_idx = int(self._get_num_jokes_()) + 1
        self.joke_df.loc[new_idx] = [setup, punchline]
        self.used.append(new_idx)
        self._update_joke_file_()

    def _update_joke_file_(self):
        """
        Update the joke file.
        """
        self.joke_df.to_csv(self.joke_file)

    def _get_num_jokes_(self):
        """
        Get the current number of jokes in the joke file.
        """
        return max(list(self.joke_df.index.values))

    def _get_random_joke_(self):
        """
        Randomly select a joke that hasn't already been told.
        """
        self.idx = self._get_random_idx_()
        self.setup = self.joke_df.loc[self.idx, SETUP]
        self.punchline = self.joke_df.loc[self.idx, PUNCHLINE]
        self.used.append(self.idx)

    def _get_random_idx_(self):
        """
        Get random index that hasn't been used yet.
        """
        idxs = list(self.joke_df.index.values)
        unused = [j for j in idxs if j not in self.used]
        if len(unused) == 0:
            print("I'm all out of jokes!")
            print("Maybe you can teach me some new ones?")
            self.used = []
            unused = idxs
        return random.choice(unused)

    def _load_jokes_(self):
        """
        Generate joke dictionary from joke file.
        """
        self.joke_df = self._load_jokes_from_file_(self.joke_file)

    @staticmethod
    def end():
        """
        Close instance of class.
        """
        quit()

    @staticmethod
    def _load_jokes_from_file_(file_path):
        """
        Load dad jokes from csv file into dictionary.
        """
        return pd.read_csv(file_path, index_col=IDX)

    @staticmethod
    def _get_response_():
        """
        Return a response to being told a joke.
        """
        responses = ['... Very funny!',
                     '... Good one!',
                     '... groan ....',
                     '... That is a definitely a DAD joke!',
                     '... Ha!',
                     '... Ill have to remember that one!']
        return random.choice(responses)