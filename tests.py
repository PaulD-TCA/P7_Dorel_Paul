#! /usr/bin/env python3
# coding: utf-8

import os, sys,inspect


from appgrandpy.modules import parserquestions
from appgrandpy.modules import basestopword
from appgrandpy.modules.parserquestions import Parser
from appgrandpy.modules.placeposition import Position
from appgrandpy.modules.wikitopic import Wikisummary
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config

def test_placeposition(monkeypatch):
    #test of posisition search with a mock
    adress_and_coord = ("7 Cité Paradis, 75010 Paris, France", {"lat": 48.8748465,
                        "lng": 2.3504873})

    def mock_placeposition(self, words_keeped, config):
        return adress_and_coord
    monkeypatch.setattr(Position, "adress_position", mock_placeposition)
    assert Position.adress_position("self", "openclassrooms", "usergooglekey") == adress_and_coord

def test_wikitopic(monkeypatch):
    #test of wikisearch search with a mock
    wikitopic_t = """OpenClassrooms est un site web de formation en ligne qui
                    propose à ses membres des cours certifiants et des parcours
                     débouchant sur des métiers en croissance."""

    def mock_wikisearch(self, words_keeped):
        return wikitopic_t
    monkeypatch.setattr(Wikisummary,"wikisearch", mock_wikisearch)
    wiki_search = Wikisummary()

    assert wiki_search.wikisearch("openclassrooms") == wikitopic_t

def test_parserquestions():
    # test of user question parser
    question_t = Parser().parser_user_question(basestopword,
            "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms?")
    assert question_t == "openclassrooms"

def test_placeposition_exept():
    # test of exeption of posisition search
    adress_and_coord = Position().adress_position("Tadidum_nonsence", config)
    assert adress_and_coord == (" ",
                                {"lat": 0, "lng": 0})

def test_wikitopic_exept():
    # test of exeption wikisearch search
    no_wikitopic = Wikisummary().wikisearch("Tadidum_nonsence")
    assert no_wikitopic == """Ho je ne comprend pas ce que tu me dis! Pose moi une autre question!"""
