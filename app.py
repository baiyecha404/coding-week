from flask import Flask, render_template, request, flash
from func import PrintCNF, PrintDNF, getTruths, getVariables, deduce
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)

ALLOWED_OPTIONS = ["truthTable", "getDNF", "getCNF"]
GENDER = ['Male', 'Female']


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/calc", methods=["GET"])
def send_calc():
    return render_template('send.html')


@app.route("/calc", methods=["POST"])
def calc():
    expression = request.form["expression"]
    options = request.form["options"]
    if expression == "":
        return "Plz send your expression."
    elif options == "":
        return "Plz send your option."
    else:
        if options not in ALLOWED_OPTIONS:
            return "Option not supported."
        try:
            variables = getVariables(expression)
            result = getTruths(variables, expression)
            # unreadable table eg:[[True,True],[],[]...]
            digit_table = result.getResult()
            if options == "truthTable":
                # readable table
                truth_table = result.getTruthTable()
                return truth_table
            elif options == "getDNF":
                flash(PrintDNF(variables, digit_table))
            elif options == "getCNF":
                flash(PrintCNF(variables, digit_table))
            return render_template('send.html')
        except Exception as e:
            return str(e)


@app.route("/judge", methods=["GET"])
def send_judge():
    return render_template('judge.html')


@app.route("/judge", methods=["POST"])
def judge():
    expression1 = request.form["expression1"]
    expression2 = request.form["expression2"]
    if expression1 == "" or expression2 == "":
        return "Plz send your expressions."
    else:
        try:
            result_1 = getTruths(getVariables(expression1), expression1).getResult()
            result_2 = getTruths(getVariables(expression2), expression2).getResult()
            if result_1 == result_2:
                flash("Judge Done. Expressions are equal.")
            else:
                flash("Judge Done. Expressions are not equal")
            return render_template('judge.html')
        except Exception as e:
            return str(e)


@app.route("/deduce", methods=["GET"])
def send_deduce():
    return render_template('deduce.html')


@app.route("/deduce", methods=["POST"])
def deduce_result():
    expression = request.form["expression"]
    if expression == "":
        return "Just copy and paste..."
    else:
        try:
            variables = getVariables(expression)
            result = getTruths(variables, expression).getResult()
            answer = deduce(variables, result)
            if answer == "Failed":
                flash('No result')
            else:
                flash("Result: " + str(answer))
                first_gender = GENDER[(0 if answer['A'] else 1)]
                second_gender = [gender for gender in GENDER if gender != first_gender][0]
                child_gender = GENDER[(0 if answer['B'] else 1)]
                flash('The first one is {0}, the second one is {1}.The child is {2}'.format(
                    first_gender, second_gender, child_gender
                ))
            return render_template('deduce.html')
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, threaded=True)
