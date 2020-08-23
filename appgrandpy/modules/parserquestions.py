#! /usr/bin/env python3
# coding: utf-8
import re


class Parser:
    """
    Parse a sentence given by user through a Flask and a web from.
    """
    def __init__(self):
        self.user_input = """Salut GrandPy! Est-ce que tu connais l'adresse
        d'OpenClassrooms?"""
        self.words_keeped = ""

    def parser_user_question(self, basestopword, u_quest):
        """
        @type basestopword: List.
        @param basestopword: A data base with french words to éliminate.
        @type u_quest: String.
        @param u_quest: A question given by users.
        @return: one or few importants words about a place.
        """
        user_question = u_quest
        question_lower_case = user_question.lower()
        question_splited = re.split("[?,!': -]", question_lower_case)
        word_keeped = []
        for word in question_splited:
            if word not in basestopword.STOP_WORDS:
                word_keeped.append(word)
        words_keeped = " ".join(word_keeped)
        self.words_keeped = words_keeped
        return words_keeped

if __name__ == "__main__":
    app.run()
