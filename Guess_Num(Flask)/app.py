from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route('/game', methods=['POST'])
def start_game():
    global range_value, target_number
    
    range_value = int(request.form['range'])
    target_number = randint(1, range_value)
    return render_template('guess.html')



@app.route('/gamestart', methods=['GET','POST'])
def check_guess():
    global feedback
    feedback = " "
    # print(target_number)
    if request.method=='POST':
        # user_guess = int(request.form['guess'])
        user_guess = int(request.form.get("guess"))
        # user_guess = int(user_guess)
        feedback = ""
        # print(target_number)
        # print(user_guess)
        # print(feedback)
        if user_guess < target_number:
            feedback = f"{user_guess} is low!"
        elif user_guess > target_number:
            feedback = f"{user_guess} is high!"
        else:
            feedback = "Congratulations! You guessed correctly."
    return render_template('guess.html', feedback=feedback)



if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)