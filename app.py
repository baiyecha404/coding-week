from flask import Flask, render_template, request, flash
from func import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)

ALLOWED_OPTIONS = ["truthTable", "getDNF", "getCNF"]
GENDER = ['Male', 'Female']


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "GET":
        return render_template('send.html')
    expression = sanatizeInput(request.form["expression"])
    options = request.form["options"]
    # not allowed to enter blank expression or option
    if expression == "":
        return "Plz send your expression."
    elif options == "":
        return "Plz send your option."
    else:
        if options not in ALLOWED_OPTIONS:
            return "Option not supported."
        if expression == "1":
            return "Logically True"
        elif expression == "0":
            return "Logically False"
        try:
            variables = getVariables(expression)
            result = getTruths(variables, expression)
            # Unreadable table eg:[[True,True],[],[]...]·
            digit_table = result.getResult()
            if options == "truthTable":
                # Return readable table in html
                truth_table = result.getTruthTable()
                return truth_table
            elif options == "getDNF":
                # Print DNF in flash
                flash(PrintDNF(variables, digit_table))
            elif options == "getCNF":
                # Print CNF in flash
                flash(PrintCNF(variables, digit_table))
            return render_template('send.html')
        except Exception as e:
            return render_template('send.html',error=str(e))


@app.route("/judge", methods=["GET", "POST"])
def judge():
    if request.method == "GET":
        return render_template('judge.html')
    expression1 = santizeInput(request.form["expression1"])
    expression2 = santizeInput(request.form["expression2"])
    if expression1 == "" or expression2 == "":
        return "Plz send your expressions."
    else:
        try:
            result_1 = getTruths(getVariables(expression1), expression1).getComparableResult()
            result_2 = getTruths(getVariables(expression2), expression2).getComparableResult()
            # Judge if two expressions are equal, then flash the result
            if result_1 == result_2:
                flash("Judge Done. Expressions are equal.")
            else:
                flash("Judge Done. Expressions are not equal")
            return render_template('judge.html')
        except Exception as e:
            return render_template('judge.html',error=str(e))


@app.route("/deduce", methods=["GET", "POST"])
def deduce_result():
    if request.method == "GET":
        return render_template('deduce.html')
    expression = santizeInput(request.form["expression"])
    if expression == "":
        return "Just copy and paste..."
    else:
        try:
            variables = getVariables(expression)
            result = getTruths(variables, expression).getResult()
            # Deduce the result
            answer = deduce(variables, result)
            if answer == "Failed":
                flash('No result')
            else:
                flash("Result: " + str(answer))
                # Deduce the first one 's gender based on  hypothesis A
                first_gender = GENDER[(0 if answer['A'] else 1)]
                # Deduce the second one's gender based on the gender of first person
                second_gender = [gender for gender in GENDER if gender != first_gender][0]
                # Deduce the first one 's gender based on  hypothesis B
                child_gender = GENDER[(0 if answer['B'] else 1)]
                # Flash the gender
                flash('The first one is {0}, the second one is {1}.The child is {2}'.format(
                    first_gender, second_gender, child_gender
                ))
            return render_template('deduce.html')
        except Exception as e:
            return render_template('deduce.html',error=str(e))

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, threaded=True)
