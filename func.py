import re
from TruthTable import Truths


def getVariables(expression):
    sp = re.compile('[a-zA-Z]')
    # simply regex out the variables
    variables = sp.findall(expression)
    return variables

def getResult(variables,expression):
    result = Truths(variables, expression)
    return result

def GenCNF(variables,t):
    """ generate CNF list """
    res = []
    for row in t:
        if row[-1] == True:
            continue
        res.append('∨'.join(map(lambda iv: ('' if iv[0] else '￢') + variables[iv[0]], enumerate(row[:-1]))))
    return res

def GenDNF(variables,t):
    """ generate DNF list """
    res = []
    for row in t:
        if row[-1] == False:
            continue
        res.append('∧'.join(map(lambda iv: ('' if iv[1] else '￢') + variables[iv[0]], enumerate(row[:-1]))))
    return res


def PrintCNF(variables,table):
    """ print CNF """
    cnfs = GenCNF(variables,table)
    return 'CNF: ' + ' ∧ '.join(cnf.join('()') for cnf in cnfs)

def PrintDNF(variables,table):
    """ print DNF """
    dnfs = GenDNF(variables,table)
    return 'DNF: ' + ' ∨ '.join(dnf.join('()') for dnf in dnfs)

