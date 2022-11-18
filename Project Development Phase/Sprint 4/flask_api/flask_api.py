from flask import Flask,render_template,request,redirect
from flask import send_file
import requests
import json
import os
from views.make_prediction import make_prediction

app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('temp.html')
    else:
        file_data = request.files.get('excel_file')
        pred = make_prediction(file_data)
        return render_template('temp.html', result = pred['response'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')