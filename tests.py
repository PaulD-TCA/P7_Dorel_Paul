#! /usr/bin/env python3
# coding: utf-8

from appgrandpy.modules import parserquestions
from appgrandpy.modules import basestopword
from appgrandpy.modules.parserquestions import Parser
from appgrandpy.modules.placeposition import Position
from appgrandpy.modules import usergooglekey
from appgrandpy.modules.wikitopic import Wikisummary


def test_placeposition(monkeypatch):

    adress_and_coord = ("7 Cité Paradis, 75010 Paris, France", {"lat": 48.8748465, "lng": 2.3504873})

    def mock_placeposition(self, words_keeped, usergooglekey):
        return adress_and_coord
    monkeypatch.setattr(Position, "adress_position", mock_placeposition)
    assert Position.adress_position("self", "openclassrooms", "usergooglekey") == adress_and_coord

def test_wikitopic(monkeypatch):

    wikitopic_t = "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance."

    def mock_wikisearch(self, words_keeped):
        return wikitopic_t
    monkeypatch.setattr(Wikisummary,"wikisearch", mock_wikisearch)
    wiki_search = Wikisummary()

    assert wiki_search.wikisearch("openclassrooms") == wikitopic_t

def test_parserquestions():
    question_t = Parser().parser_user_question(basestopword, "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms?")
    assert question_t == "openclassrooms"

def test_placeposition():
    adress_and_coord = Position().adress_position("Tadidum_nonsence", usergooglekey)
    assert adress_and_coord == ("Je ne me rapelle pas où cela ce trouve.", {"lat": 0, "lng": 0})

def test_wikitopic_exept():
     no_wikitopic = Wikisummary().wikisearch("Tadidum_nonsence")
     assert no_wikitopic == "Ho je ne comprend pas ce que tu me dis!"
