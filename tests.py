#! /usr/bin/env python3
# coding: utf-8

from appgrandpy.modules import parserquestions
from appgrandpy.modules import basestopword
from appgrandpy.modules.parserquestions import Parser
from appgrandpy.modules.placeposition import Position
from appgrandpy.modules import usergooglekey
from appgrandpy.modules.wikitopic import Wikisummary

print("lolo")
#print(basestopword.STOP_WORDS)

def test_parserquestions():
    question_t = Parser().parser_user_question(basestopword, "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms?")
    assert question_t == "openclassrooms"


def test_placeposition():
    adress_and_coord = Position().adress_position("openclassrooms", usergooglekey)
    assert adress_and_coord == ["7 Cité Paradis, 75010 Paris, France", {"lat": 48.8748465, "lng": 2.3504873}]


def test_wikitopic(monkeypatch):

    wikitopic_t = "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance."

    def mock_wiki(words_keeped):
        return wikitopic_t
    monkeypatch.setattr(Wikisummary, "wikisearch", mock_wiki)
    assert Wikisummary.wikisearch("openclassrooms") == wikitopic_t
