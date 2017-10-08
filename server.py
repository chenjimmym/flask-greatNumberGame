from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'aSecret'

answer = random.randrange(0,101)
@app.route('/')
def reset():
    session['answer'] = random.randrange(0,101)
    print session['answer']
    return redirect('/start')
@app.route('/start')
def indexPage():
    # session['answer'] = answer
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submitted():
    if int(request.form['guessed']) < session['answer']:
        session['hint'] = 'Too Low!'
    elif int(request.form['guessed']) > session['answer']:
        session['hint'] = 'Too High!'
    else:
        # session['answer'] = random.randrange(0,101)
        return render_template('result.html')

    return redirect('/start')


app.run(debug=True)