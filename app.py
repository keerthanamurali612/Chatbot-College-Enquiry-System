from flask import Flask,render_template,request
from nltk.chat.util import reflections,Chat 
import re
from pairs import pairs

chat = Chat(pairs,reflections)

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/get")
def home():
    msg = request.args.get("msg")
    return chat.respond(msg)