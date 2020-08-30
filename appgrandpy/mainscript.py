#! /usr/bin/env python3
# coding: utf-8


import os, sys,inspect

from appgrandpy.modules import parserquestions
from appgrandpy.modules import placeposition
from appgrandpy.modules import basestopword
from appgrandpy.modules import wikitopic
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config


# Instances creation.
parser = parserquestions.Parser()
position = placeposition.Position()
wiki = wikitopic.Wikisummary()


class main_py_script:
    """
    Centralize the backend objects execution and return to Flask templates a
    topic taken from Wikipedia and a position taken from Google Maps.
    """
    def __init__(self):
        self.words_keeped = "openclassrooms"
        self.position = ("7 Cité Paradis, 75010 Paris, France",
                        {"lat": 48.8748465, "lng": 2.3504873})
        self.wiki_answer = """OpenClassrooms est un site web de formation en ligne
                         qui propose à ses membres des cours certifiants et des
                         parcours débouchant sur des métiers en croissance."""


    def main(self, u_quest):
        """
        @type u_quest: String.
        @param u_quest: A question given by users.
        @return: One or few importants words about a place, an adress and his
         position and a topic taken from Wikipedia.
        """
        self.words_keeped = parser.parser_user_question(basestopword, u_quest)
        self.position = position.adress_position(self.words_keeped, config)
        self.wiki_answer = wiki.wikisearch(self.words_keeped)
