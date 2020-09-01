#! /usr/bin/env python3
# coding: utf-8
import requests
import json

class Position:
    """
    Send a request to Google Maps to find an adress place and his position.
    """
    def adress_position(self, words_keeped, config):
        """
        @type words_keeped: List.
        @param words_keeped: Few importants words about a place or a topic.
        @type usergooglekey: String.
        @param usergooglekey: A user google API key.
        @return: An adress and his position or a sentance
        if noting is returned by Google Maps.
        """
        try:
            api_url = "https://maps.googleapis.com/maps/api/geocode/json?"
            search_params = {"address": words_keeped, "key": config.USER_GOOGLE_KEY}
            resp = requests.get(api_url, search_params)
            geocode_result = resp.json()

            raw_adress = geocode_result["results"][0]["formatted_address"]
            adress = "Je me rapelle que cela se trouve à l'adresse suivante: " + raw_adress + ". "
            latlong = geocode_result["results"][0]["geometry"]["location"]

            return adress, latlong
        except:
            return " ", {"lat": 0, "lng": 0}
