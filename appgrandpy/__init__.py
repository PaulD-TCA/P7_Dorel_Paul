#! /usr/bin/env python3
# coding: utf-8


from flask import Flask, render_template, request, url_for
from flask import jsonify
from appgrandpy.modules import basestopword
app = Flask(__name__)
from appgrandpy import mainscript


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homegrandpy.html')

@app.route("/api/info/", methods=['POST'])
def route():
    user_quest = request.data
    question_decode = user_quest.decode('utf-8')
    u_quest = str(question_decode)
    maininstance = mainscript.main_py_script()
    maininstance.main(u_quest)
    w_keeped = maininstance.words_keeped
    topic_from_wiki = maininstance.wiki_answer
    adress_position = maininstance.position
    return jsonify(w_keeped, topic_from_wiki, adress_position)
