from flask import Flask, redirect, render_template, Request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')



