from flask import Flask, render_template, request
app = Flask(__name__)
words = ['Москва','Арбуз','Кот']
@app.route("/")
def hello():
    global player
    global i
    global t
    i = 0
    player = '1 player'
    return render_template('hat.html', words = words, i = i, t = 20, player = player)
@app.route("/word", methods = ['GET', 'POST'])
def word():
    global player
    global t
    global i
    i += 1
    if request.method == 'POST':
        t = request.form['time']
        if t == '' and player == '1 player':
            player = '2 player'
            t = 20
        elif t == '' and player == '2 player':
            player = '1 player'
            t = 20
    return render_template('hat.html', words = words, i = i, t = t, player = player)
if __name__ == "__main__":
    app.run()
