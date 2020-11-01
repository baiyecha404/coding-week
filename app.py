from flask import Flask, render_template, request, flash, redirect, send_file, session
from func import PrintCNF,PrintDNF,getResult,getVariables

app = Flask(__name__)

ALLOWED_OPTIONS = ["truthtable", "getDNF", "getCNF", "deduce"]

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
            return "Options not supported."
        try:
            variables = getVariables(expression)
            result=getResult(variables,expression)

            # unreadable table eg:[[True,True],[],[]...]
            digit_table = result.getResult()
            if options == "truthtable":
                # readable table
                truth_table = result.getTruthTable()
                return truth_table
            elif options == "getDNF":
                return PrintDNF(variables,digit_table)
            elif options == "getCNF":
                return PrintCNF(variables,digit_table)
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
            result_1=getResult(getVariables(expression1),expression1).getResult()
            result_2 = getResult(getVariables(expression1), expression1).getResult()
            if result_1 == result_2:
                return "Judge Done. Expressions are equal."
            else:
                return "Judge Done. Expressions are not equal"

        except Exception as e:
            return str(e)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, threaded=True)