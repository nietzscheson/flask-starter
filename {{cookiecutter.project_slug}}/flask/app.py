import os
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", os.environ['NAME'])
    return f'Hello, {escape(name)}!'
