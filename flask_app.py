
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for
import random

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def index():
        f = open("/home/patrickveegee/mysite/data/subjuntivo_finalidad.csv","r")
        lines = f.readlines()
        my_pairs = []
        for line in lines:
            words = line.split("\t")
            my_pairs.append((words[0],words[1]))
#        my_pairs = (("Quiero que te (ir, tú) ya","Quiero que te vayas ya"),("Necesito que me (ayuar,tú) con esto","Quiero que me ayudes con esto"))
        my_pair = my_pairs[random.randrange(len(my_pairs))]
        front = my_pair[0]
        back = my_pair[1]
        return render_template("main_page.html", front=front,back=back)

#    return redirect(url_for('index'))

