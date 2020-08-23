#! /usr/bin/env python3
# coding: utf-8


import requests
import json
import re

class Wikisummary:
    """
    Send a request to Wikipedia to get the fist sentance of a topic.
    """
    def wikisearch(self, words_keeped):
        """
        @type words_keeped: List.
        @param words_keeped: Few importants words about a place or a topic.
        @return: The first sentance of a topic taken from Wikipedia or another
        sentance if noting is returned by Wikipedia.
        """
        try:
            api_url = 'http://fr.wikipedia.org/w/api.php'
            search_params = {'action': 'query', 'prop': 'extracts', 'format': 'json', 'indexpageids': 1, 'exsentences':1, "generator": 'search', 'gsrlimit':1, 'gsrsearch': words_keeped}
            resp = requests.get(api_url, search_params)
            wiki_data = resp.json()
            wiki_pageids = wiki_data["query"]["pageids"][0]
            wiki_sentance = wiki_data["query"]["pages"][wiki_pageids]["extract"]
            topicwikipedia = re.sub('<[^<]+?>', '', wiki_sentance)
            print(topicwikipedia)
            return topicwikipedia
        except:
            return """Ho je ne comprend pas ce que tu me dis. Pose moi une autre
            question!"""
