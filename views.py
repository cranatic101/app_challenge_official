from datetime import datetime
from flask import Flask, render_template,request
from . import app
from hello_app import posts

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/createpost/")
def createpost():
    return render_template("createpost.html")

@app.route('/success', methods=['POST'])
def success():
    title = request.form['title']
    topic=request.form['topic']
    content=request.form['content']
    test=posts.Post('user','1/1/1',title,topic,content)
    #test.create_post()
    return render_template('success.html', title=title,topic=topic,content=content)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
