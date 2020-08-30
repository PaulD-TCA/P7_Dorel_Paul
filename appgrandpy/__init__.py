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
    u_quest = request.data
    u_quest = str(u_quest)
    maininstance = mainscript.main_py_script()
    maininstance.main(u_quest)
    w_keeped = maininstance.words_keeped
    topic_from_wiki = maininstance.wiki_answer
    adress_position = maininstance.position
    return jsonify(w_keeped, topic_from_wiki, adress_position)
