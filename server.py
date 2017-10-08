from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'aSecret'

answer = random.randrange(0,101)
@app.route('/')
def indexPage():
    #session.pop('hint')
    session['answer'] = answer
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submitted():
    if int(request.form['guessed']) < session['answer']:
        session['hint'] = 'Too Low!'
    elif int(request.form['guessed']) > session['answer']:
        session['hint'] = 'Too High!'
    else:
        session['hint'] = 'Got It!!!'
    # print type(int(request.form['guessed']))
    # print type(session['answer'])
    return redirect('/')

app.run(debug=True)