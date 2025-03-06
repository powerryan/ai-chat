from flask import render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from __main__ import app
import json
from ollama import Client

ollama_client = Client(host='http://localhost:11434')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    response = ollama_client.generate(model='mistral', prompt=question)
    return {"answer": f"{response.response}"}, 200

@app.route('/home', methods=['POST', 'GET'])
def homePage():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def landing():
    return render_template("index.html")
